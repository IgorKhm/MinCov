"""
Created on Jul 9, 2019

@author: ikhmelnitsky
"""
import heapq
import multiprocessing as mp
import time
from builtins import range
from copy import deepcopy
from heapq import heappush, heappop

import numpy as np

from node_cover_tree import CovNode
from omega_transition import OmegaTransition
from petri_net import PetriNet
from qcover.coverability import igor_check_cpn_coverability_z3
from qcover.cpn import build_cpn_solver
from qcover.petri import load_petrinet
from z3_for_accelarations import get_accelerations_from_z3

lesseq = np.less_equal


def _is_closed_to_transitions(nodes: [CovNode], trans: [OmegaTransition], set_of_node: {tuple}):
    """
    Recives a set of makrkings(in node format N) and transitions(T) and checks if ↑N =  ↑{N+t: t\in T}
    """
    new_front = []
    for node1 in nodes:
        for tran in trans:
            if tran.is_fireable_from(node1.marking):
                new_mark = tran.apply_on_marking(deepcopy(node1.marking))
                covered = False
                if tuple(new_mark) in set_of_node:
                    covered = True
                else:
                    for node2 in nodes:
                        if all(new_mark <= node2.marking):
                            covered = True
                            continue
                if not covered:
                    new_node = CovNode(new_mark, node1._dim, node1._depth + 1, node1)
                    new_node.add_transition(tran)
                    new_node.trans_to_fire = len(trans) - 1
                    new_front.append(new_node)
                    # new_front.append([2])

    return new_front


def _is_anti_chain(nodes: [CovNode]):
    """
    Checks if the set of markings is an antichain
    :param nodes:
    :return:
    """
    num_nodes = len(nodes)
    for i in range(num_nodes):
        node1 = nodes[i]
        for j in range(num_nodes):
            node2 = nodes[j]
            if all(node1.marking <= node2.marking):
                if node1 != node2:
                    return False
    return True


def _from_vec_mark_to_places_mark(mark: np.array):
    """
    prints the marking as a string of places. (0,2,1) => 2*p2, p*3
    """
    print("mark: ")
    for p in range(len(mark)):
        if mark[p] != 0:
            print("%.0f*p%d, " % (mark[p], p), end='')
    print("")


GRAPH_TRAVERSALS = {'DFS': 1, 'BFS': 2, 'MOST_TOKEN_FIRST': 3, 'RANDOM': 4}


class CovTree:
    def __init__(self, petri_net: PetriNet, mark: np.array):
        """
        Constructor
        """
        assert (isinstance(petri_net, PetriNet)), "Has to be a Petri Net"
        self._petriNet = petri_net
        self._dim = petri_net.get_dim()
        self._accelerations = np.array([])

        self._root = CovNode(mark, self._dim, 0, None)
        self._vertices = [self._root]  # a list of all the vertices
        self._front = [self._root]  # a list of the vertices which still weren't processed
        self._verSet = {tuple(self._root.marking)}  # A set of all the marks, used to increase speed(hash)

        # Options for the run of generate_cov_tree():
        self.timeout = float("inf")  # The time out for generate_cov_tree()

        self.keep_accelerations = True  # Remember and reuse previous accelerations

        self.use_z3_to_guess_accelerations = False  # Use z3 to try to guess some accelerations before starting for
        self.z3_timeout = 10  # z3 guessing timeout

        self.check_for_correctness = True  # in the end of generate_cov_tree() preform a few checks for correctness

        # setting the graph traversal:
        self._type_of_graph_traversal = 1
        self.pushFront = self.push_into_front_function()
        self.popFront = self.pop_next_vertex_func()
        self.deleteFromFront = self.remove_from_front_function()

        # Variables for tracking performance:
        self.verbose = False
        self.max_size = 1
        self.max_size_of_acc = 0
        self.use_of_acc = 0
        self.count = 0
        self.max_depth = 0
        self.number_of_deleted_nodes = 0
        self.number_of_deleted_decedents = 0
        self.max_depth_of_acc = 0
        self.average_num_of_successors = 0
        self.num_of_comparisons = 0
        self.average_vertics_size = 1
        self.num_of_accelaration_tried = 0
        self.num_of_rechecks = 0

    @property
    def type_of_graph_traversal(self):
        return self._type_of_graph_traversal

    @type_of_graph_traversal.setter
    def type_of_graph_traversal(self, type_travel):
        assert (type_travel in GRAPH_TRAVERSALS)
        self._type_of_graph_traversal = GRAPH_TRAVERSALS.get(type_travel)
        self.pushFront = self.push_into_front_function()
        self.popFront = self.pop_next_vertex_func()
        self.deleteFromFront = self.remove_from_front_function()

    def delete_node(self, node: CovNode, delete_from_verSet=True):
        """
        Deletes a node.

        delete_from_verSet: sometimes we don't need to delete from verSet.
        """
        self.number_of_deleted_nodes += 1
        self._delete_descendants(node)

        if node.get_parent() is not None:
            node.get_parent().delete_child(node)
        self._vertices.remove(node)
        if delete_from_verSet:
            self._verSet.remove(tuple(node.marking))
        if node in self._front:
            self.deleteFromFront(node)

    def _delete_descendants(self, node: CovNode):
        """
        Deletes all the descendants of a specific node

        Python has a limitation on the depth of recursion.
        Hence we do it with a loop instead of raising the
        limit recursion.
        """
        new_children = node.get_children()
        while len(new_children) != 0:

            child = new_children.pop()
            new_children.extend(child.get_children())

            # Begin - Code for performance tracing #
            self.number_of_deleted_decedents += 1
            self.number_of_deleted_nodes += 1
            # END - Code for performance tracing#

            self._vertices.remove(child)
            self._verSet.remove(tuple(child.marking))
            if child in self._front:
                self.deleteFromFront(child)

    def _accelerate(self, current_node: CovNode):
        """
        Tries to accelerate the marking of the current node according to its ancestors
        :return: If accelerated return the father of the ancestor that we accelerated from, otherwise return None
        """
        ancestor_node = current_node.get_parent()

        while ancestor_node is not None:
            # Begin - Code for performance tracing #
            # self.num_of_comparisons += 1
            # END - Code for performance tracing #

            if all(current_node.marking >= ancestor_node.marking):
                current_node.applyed_acc = True
                # about to change the marking, hence need to get it out of the set
                self._verSet.remove(tuple(current_node.marking))

                if self.keep_accelerations:
                    # If using the new algorithm then we create an acceleration for further use:
                    (pre, incidence) = self._compute_pre_and_incidence_acceleration(current_node, ancestor_node)
                    acc = OmegaTransition(pre, incidence)
                    self._add_acceleration(acc)

                    current_node.marking = acc.apply_on_marking(current_node.marking)
                    current_node._tranFromParent = ancestor_node.get_transitions()
                    current_node.add_transition(acc)
                    self._verSet.add(tuple(current_node.marking))

                else:
                    # If using Alain's Finkel original algorithm then just accelerate:
                    acc = np.where(current_node.marking > ancestor_node.marking, (float("inf")), 0)
                    current_node.marking = current_node.marking + acc
                    self._verSet.add(tuple(current_node.marking))

                return ancestor_node

            ancestor_node = ancestor_node.get_parent()

        return None

    def _add_acceleration(self, acc: OmegaTransition):
        """
        Add an acceleration to the set of existing acc, while keeping the accelerations an antichain.
        acc1<=acc2 if ((acc1.pre)<=(acc2.pre) & (acc2.post)>=(acc2.post))
        """
        assert (isinstance(acc, OmegaTransition)), \
            "the acc has to be an omega transition"
        accelerations = self._accelerations
        num_of_acc = len(accelerations)
        for i in range(num_of_acc):
            if acc >= accelerations[num_of_acc - i - 1]:
                np.delete(accelerations, num_of_acc - i - 1)
        self._accelerations = np.append(self._accelerations, acc)

    def _compute_pre_and_incidence_acceleration(self, current_node: CovNode, ance_node: CovNode):
        """
        Given a node(current_node) and one of its ancestors(ance_node) which is has a smaller marking.
        Finds the the pre and incidence of the acceleration between them.
        :return:
        """
        pre = np.zeros(self._dim)
        incidence = np.zeros(self._dim)

        while current_node != ance_node:
            # Begin - Code for performance tracing #
            # self.num_of_comparisons += 1  # notsure
            # END - Code for performance tracing #

            trans = current_node.get_transitions()
            for i in range(len(trans)):
                tran = trans[len(trans) - i - 1]
                incidence = incidence + tran.get_incidence()

                for p in range(self._dim):
                    if (pre[p] == float("inf")) & ((tran.get_incidence())[p] == float("inf")):
                        pre[p] = 0
                        continue
                    if (pre[p] - (tran.get_incidence())[p]) < (tran.get_pre())[p]:
                        pre[p] = (tran.get_pre())[p]
                    else:
                        pre[p] = pre[p] - (tran.get_incidence())[p]

            current_node = current_node.get_parent()

        for p in range(self._dim):
            if incidence[p] < 0:
                pre[p] = float("inf")

        for p in range(self._dim):
            if incidence[p] != 0:
                incidence[p] = float("inf")

        return pre, incidence

    def _find_and_delete_smaller(self, current_node: CovNode, nodes_to_delete: [CovNode], accelerated):
        """
        Deletes all the nodes with smaller marking then current Node.
        If we haven't found a new acceleration in the iteration where we poped the current node from Front, we already
        have a list of the nodes we need to delete. Otherwise we need to make sure we don't have new nodes to delete.
        """
        if not accelerated:
            for node in nodes_to_delete:
                self.delete_node(node)
            return
        else:
            for node in nodes_to_delete:
                if tuple(node.marking) in self._verSet:
                    self.delete_node(node)

        current_marking = current_node.marking
        self._vertices.reverse()
        for node in self._vertices:

            # Begin - Code for performance tracing #
            # self.num_of_comparisons += 1
            # END - Code for performance tracing #

            if all(current_marking >= node.marking):
                if node != current_node:
                    self.delete_node(node)
        self._vertices.reverse()

    def _check_ancestors(self, current_node: CovNode):
        accelerated = False
        ance_node = self._accelerate(current_node)
        while ance_node is not None:
            accelerated = True
            current_node.change_parent(ance_node.get_parent())
            if (current_node._depth - ance_node._depth) > self.max_depth_of_acc:
                self.max_depth_of_acc = current_node._depth - ance_node._depth
            current_node._depth = ance_node._depth
            self.delete_node(ance_node)
            ance_node = self._accelerate(current_node)
        return accelerated

    # not used anymore: #
    def _explore_successor(self, current_node: CovNode):
        new_nodes = current_node.successors_no_duplicates(self._petriNet.get_transitions())
        num_children = len(new_nodes)
        self.average_num_of_successors = (self.average_num_of_successors * (self.count - 1) + num_children) / self.count
        for i in range(num_children):
            child = new_nodes[num_children - i - 1]
            # We don't want to add vertices with the same marking to verSet.
            # Moreover, it pays off to check if we already discovered some of these marking:
            if tuple(child.marking) in self._verSet:
                current_node.delete_child(child)
                continue
            else:
                self._vertices.append(child)
                self._front.append(child)
                self._verSet.add(tuple(child.marking))

    def pop_next_vertex_func(self):
        if self._type_of_graph_traversal == GRAPH_TRAVERSALS.get("DFS"):
            return lambda: self._front.pop()
        elif self._type_of_graph_traversal == GRAPH_TRAVERSALS.get("BFS"):
            return lambda: self._front.pop(0)
        elif self._type_of_graph_traversal == GRAPH_TRAVERSALS.get("MOST_TOKEN_FIRST"):
            return lambda: heappop(self._front)
        else:
            return lambda: self._front.pop(np.random.random_integers(0, len(self._front) - 1))

    def push_into_front_function(self):
        if self._type_of_graph_traversal == GRAPH_TRAVERSALS.get("MOST_TOKEN_FIRST"):
            return lambda node: heappush(self._front, node)
        else:
            return lambda node: self._front.append(node)

    def remove_from_front_most_tokens_first(self, node: CovNode):
        i = self._front.index(node)
        self._front[i] = self._front[-1]
        self._front.pop()
        if i < len(self._front):
            heapq._siftup(self._front, i)
            heapq._siftdown(self._front, 0, i)

    def remove_from_front_function(self):
        if self._type_of_graph_traversal == GRAPH_TRAVERSALS.get("MOST_TOKEN_FIRST"):
            return self.remove_from_front_most_tokens_first
        else:
            return lambda node: self._front.remove(node)

    def generate_cov_tree(self, root_mark=None):
        if root_mark is not None:
            self.reset_vertices(root_mark)

        if self._type_of_graph_traversal == GRAPH_TRAVERSALS.get("MOST_TOKEN_FIRST"):
            self._front = []
            heappush(self._front, self._root)

        start_time = time.time()
        if self.use_z3_to_guess_accelerations:
            self._accelerations = get_accelerations_from_z3(self._petriNet.get_transitions(), self._root.marking,
                                                            self.z3_timeout)

        trans = np.array(self._petriNet.get_transitions())
        num_trans = len(trans)
        self._root.trans_to_fire = num_trans - 1
        clover_is_not_ready = True

        while clover_is_not_ready:

            while len(self._front) != 0:
                if self.timeout < time.time() - start_time:
                    return None
                current_node = None
                current_parent_node = self.popFront()
                while 1:
                    if current_parent_node.trans_to_fire == 0:
                        if len(self._front) != 0:
                            current_parent_node = self.popFront()
                        else:
                            break

                    tran = trans[current_parent_node.trans_to_fire - 1]
                    current_parent_node.trans_to_fire -= 1

                    # Begin - Code for performance tracing #
                    # self.num_of_comparisons += 1
                    # END - Code for performance tracing #

                    if tran.is_fireable_from(current_parent_node.marking):
                        new_marking = tran.apply_on_marking(current_parent_node.marking)
                        if tuple(new_marking) not in self._verSet:
                            current_node = CovNode(new_marking, current_parent_node._dim,
                                                   current_parent_node._depth + 1, current_parent_node, self.count + 1)
                            current_node.add_transition(tran)
                            current_node.trans_to_fire = num_trans
                            break

                if current_parent_node.trans_to_fire > 0:
                    self.pushFront(current_parent_node)
                if not current_node:
                    continue

                # Begin - Code for performance #
                if (self.count % 1000 == 0) & (self.count != 0):
                    if self.verbose:
                        print("---------------------")
                        print("V: %d" % len(self._vertices))
                        print("Front: %d" % len(self._front))
                        print("acc: %d" % len(self._accelerations))
                        print("acc used: %d" % self.use_of_acc)
                        print("max depth of acc: %d" % self.max_depth_of_acc)
                        print("current depth: %d" % current_node._depth)
                        print("max depth: %d" % self.max_depth)
                        print("num of deleted nodes(not during creation): %d" % self.number_of_deleted_nodes)
                        print("num of deleted decedents: %d" % self.number_of_deleted_decedents)
                        print("average num of successors: %f" % self.average_num_of_successors)
                        print("time: %f" % (time.time() - start_time))
                        print("count: %d" % self.count)
                        print("---------------------")
                    self.count += 1
                else:
                    self.count += 1
                    self.average_vertics_size = (self.average_vertics_size * (self.count - 1) + len(
                        self._vertices)) / self.count
                # End - Code for performance #

                if self.keep_accelerations:
                    self._use_accelerations(current_node)
                if tuple(current_node.marking) in self._verSet:
                    current_parent_node.delete_child(current_node)
                    continue

                nodes_to_delete = self._check_if_there_exists_bigger_marking(current_node)
                if nodes_to_delete is None:
                    current_parent_node.delete_child(current_node)
                    continue

                self._vertices.append(current_node)
                self._verSet.add(tuple(current_node.marking))
                self.pushFront(current_node)

                accelarated = self._check_ancestors(current_node)

                self._find_and_delete_smaller(current_node, nodes_to_delete, accelarated)

                # Begin - Code for performance #
                if self.max_size < len(self._vertices):
                    self.max_size = len(self._vertices)
                if self.max_size_of_acc < len(self._accelerations):
                    self.max_size_of_acc = len(self._accelerations)
                self.max_depth = max(current_node._depth, self.max_depth)
                # End - Code for performance #

            if self.keep_accelerations:
                clover_is_not_ready = False
            else:
                print(time.time())
                new_front = _is_closed_to_transitions(self._vertices, self._petriNet.get_transitions(), self._verSet)
                print(time.time())
                if len(new_front) == 0:
                    clover_is_not_ready = False
                else:
                    for node in new_front:
                        self.num_of_rechecks += 1
                        self._vertices.append(node)
                        self._verSet.add(tuple(node.marking))
                        self.push_next_vertex(node)

        # Begin - Code for performance #
        if self.max_size > 0:
            print("MAX size of V:  %d" % self.max_size)
            print("MAX size of Acc: %d" % self.max_size_of_acc)
            print("size of V: %d" % len(self._vertices))
            print("size of VerSet: %d" % len(self._verSet))
            print("size of Acc: %d" % len(self._accelerations))
            print("Num of acc used: %d" % self.use_of_acc)
            print("Total time(rounded): %f" % (time.time() - start_time))
            print("max depth: %d" % self.max_depth)
            print("num of deleted nodes(not during creation): %d" % self.number_of_deleted_nodes)
            print("num of deleted decedents: %d" % self.number_of_deleted_decedents)
            print("max depth of acc: %d" % self.max_depth_of_acc)
            print("count: %d" % self.count)
            print("num of comperesions: %d" % self.num_of_comparisons)
            print("average vertices size: %f" % self.average_vertics_size)
            print("num of rechecks : %d" % self.num_of_rechecks)

        # End - Code for performance #

        if self.check_for_correctness:
            self._check_for_correctness()

        return self._vertices

    def check_for_cover(self, target: np.array, root_mark=None):
        if root_mark is not None:
            self.reset_vertices(root_mark)

        start_time = time.time()
        if self.use_z3_to_guess_accelerations:
            self._accelerations = get_accelerations_from_z3(self._petriNet.get_transitions(), self._root.marking,
                                                            self.z3_timeout)

        if self._type_of_graph_traversal == GRAPH_TRAVERSALS.get("MOST_TOKEN_FIRST"):
            self._front = []
            heappush(self._front, self._root)

        trans = np.array(self._petriNet.get_transitions())
        num_trans = len(trans)
        self._root.trans_to_fire = num_trans - 1
        while len(self._front) != 0:
            if time.time() - start_time > self.timeout:
                return None
            self.count += 1
            current_node = None
            current_parent_node = self.popFront()

            while 1:
                tran = trans[current_parent_node.trans_to_fire]
                current_parent_node.trans_to_fire -= 1
                # self.num_of_comparisons += 1
                if tran.is_fireable_from(current_parent_node.marking):
                    new_marking = tran.apply_on_marking(current_parent_node.marking)
                    if tuple(new_marking) not in self._verSet:
                        current_node = CovNode(new_marking, current_parent_node._dim,
                                               current_parent_node._depth + 1, current_parent_node)
                        current_node.add_transition(tran)
                        current_node.trans_to_fire = num_trans - 1
                        break

                if current_parent_node.trans_to_fire < 0:
                    if len(self._front) != 0:
                        current_parent_node = self.popFront()
                    else:
                        break

            if current_parent_node.trans_to_fire >= 0:
                self.pushFront(current_parent_node)
            if not current_node:
                continue

            if self.keep_accelerations:
                self._use_accelerations(current_node)
            if tuple(current_node.marking) in self._verSet:
                current_parent_node.delete_child(current_node)
                continue

            nodes_to_delete = self._check_if_there_exists_bigger_marking(current_node)
            if nodes_to_delete is None:
                current_parent_node.delete_child(current_node)
                continue

            self._vertices.append(current_node)
            self._verSet.add(tuple(current_node.marking))
            self.pushFront(current_node)

            accelarated = self._check_ancestors(current_node)

            self._find_and_delete_smaller(current_node, nodes_to_delete, accelarated)

            if all(current_node.marking >= target):
                print("------Covered-----------")
                print("V: %d" % len(self._vertices))
                print("time: %f" % (time.time() - start_time))
                print("count: %d" % self.count)
                print("---------------------")
                return True

        print("------Not covered-----------")
        print("V: %d" % len(self._vertices))
        print("time: %f" % (time.time() - start_time))
        print("count: %d" % self.count)
        print("---------------------")

        return False

    def _check_for_correctness(self):
        if _is_anti_chain(self._vertices):
            print("Got an antichain")
        else:
            print("not an anti chain")
        if _is_closed_to_transitions(self._vertices, self._petriNet.get_transitions(), self._verSet):
            print("the set is closed to transitions firing")
        else:
            print("not closed to transitions firing")

    def _check_if_there_exists_bigger_marking(self, current_node: CovNode, found_smaller=False):
        current_mark = current_node.marking
        smaller_nodes = []
        # self._vertices.reverse()
        for node in self._vertices:
            # self.num_of_comparisons += 1
            if not found_smaller:
                if all(lesseq(current_mark, node.marking)):
                    if node != current_node:
                        # self._vertices.remove(current_node)
                        # current_node.get_parent().delete_child(current_node)

                        # self._vertices.reverse()
                        return None
            # self.num_of_comparisons += 1
            if all(lesseq(node.marking, current_mark)):
                if node != current_node:
                    found_smaller = True
                    # self.delete_node(node)
                    smaller_nodes.append(node)
        # self._vertices.reverse()
        smaller_nodes.reverse()
        return smaller_nodes

    def _use_accelerations(self, current_node: CovNode):
        i = len(self._accelerations) - 1
        while i > 0:
            # for i in range(len(self._accelerations)):
            acc = self._accelerations[i]
            # self.num_of_comparisons += 1
            self.num_of_accelaration_tried += 1
            if acc.is_fireable_from(current_node.marking):
                pre_marking = current_node.marking
                current_node.marking = acc.apply_on_marking(current_node.marking)
                if any(pre_marking != current_node.marking):
                    # self._verSet.remove(tuple(pre_marking))
                    # self._verSet.add(tuple(current_node.marking))
                    i = len(self._accelerations) - 1
                    current_node.applyed_acc = True
                    self.use_of_acc += 1
            i -= 1

    def reset_vertices(self, root_mark: np.array):
        self._root = CovNode(root_mark, self._dim, 0, None)
        self._vertices = [self._root]
        self._front = [self._root]
        self._verSet = {tuple(self._root.marking)}

        self.max_size = 1
        self.max_size_of_acc = 0
        self.use_of_acc = 0
