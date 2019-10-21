"""
Copyright 2019 Igor Khmelnitsky, Alain Finkel, Serge Haddad

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import cProfile
import os
import unittest

import numpy as np

from cover_tree_with_hash import CovTreeHash
from cover_tree_with_tests import CovTreeHashTest
from load_petri_net_from_file import load_petri_net_from_spec, load_marking_from_mp
from node_cover_tree import CovNode
from omega_markings import OmegaMarking
from omega_transition import OmegaTransition
from petri_net import PetriNet


class Test(unittest.TestCase):

    def test_transitions(self):
        """
        Testting basic properties of transitions
        """
        #       Checking transitoin creation exceptions(diff dim for pre and post,
        #       C+Pre < 0
        with self.assertRaises(Exception):
            OmegaTransition(np.array([1, 2, 3, 5, 6]), np.array([1, 4, 3, -1]))
        with self.assertRaises(Exception):
            OmegaTransition(np.array([1, 2, 3, 5]), np.array([1, 4, 3, -20]))

        #       Loading test data
        tran1 = OmegaTransition(np.array([1, 2, 3, 5]),
                                np.array([1, 4, 3, -5]))
        tran2 = OmegaTransition(np.array([1, float("inf"), 3, 5]),
                                np.array([2, 3, 3, -5]))
        tran3 = OmegaTransition(np.array([1, float("inf"), 2, 5]),
                                np.array([5, 5, float("inf"), -5]))

        #       Checking oreder and equality
        self.assertNotEqual(tran1, tran2)
        self.assertEqual(tran1, tran1)
        self.assertGreaterEqual(tran3, tran2)
        self.assertFalse((tran1 >= tran2) | (tran1 <= tran2))

    def test_markings(self):
        """
        Testting basic properties of markings
        """
        #       Loading test data
        mark1 = OmegaMarking(np.array([1, 2, 3, float("inf")]))
        mark2 = OmegaMarking(np.array([1, float("inf"), 4, float("inf")]))
        mark3 = OmegaMarking(np.array([1, 2, 4, 5]))
        tran1 = OmegaTransition(np.array([1, 2, 3, 6, 4]),
                                np.array([1, 4, 3, -5, 5]))
        tran2 = OmegaTransition(np.array([1, 2, 3, float("inf")]),
                                np.array([0, float("inf"), 1, float("inf")]))

        #       Checking equalty and order
        self.assertNotEqual(mark1, mark2)
        self.assertEqual(mark1, mark1)
        self.assertGreaterEqual(mark2, mark1)
        self.assertFalse((mark1 >= mark3) | (mark3 <= mark1))
        self.assertGreaterEqual(mark2, mark3)

        #       Checking transition firings
        with self.assertRaises(Exception):
            OmegaTransition(mark1.is_fireable(tran1), None)
        self.assertTrue(mark1.is_fireable(tran2))
        with self.assertRaises(Exception):
            OmegaTransition(mark1.fire_transition(tran1), None)
        mark1.fire_transition(tran2)
        self.assertEqual(mark1, mark2)

    def test_petri_net(self):
        """
        Testting basic properties of petri net
        """
        with self.assertRaises(Exception):
            PetriNet(0.5)
        with self.assertRaises(Exception):
            PetriNet(0)

        mark1 = OmegaMarking(np.array([1, 2, 3, float("inf")]))
        mark2 = OmegaMarking(np.array([1, 2, 3, float("inf"), 5]))
        tran1 = OmegaTransition(np.array([1, 2, 3, 5]),
                                np.array([1, 4, 3, -5]))
        tran2 = OmegaTransition(np.array([1, float("inf"), 3, 5]),
                                np.array([2, 3, 3, -5]))
        tran3 = OmegaTransition(np.array([1, float("inf"), 2, 5]),
                                np.array([5, 5, float("inf"), -5]))

        petri = PetriNet(4)
        with self.assertRaises(Exception):
            petri.mark_the_petri_net(mark2)

        petri.mark_the_petri_net(mark1)
        petri.add_transition(tran1)
        petri.add_transition(tran2)
        petri.add_transition(tran3)

        self.assertEqual(len(petri.get_transitions()), 3)

    def test_cov_node(self):
        """
        Testing basic properties of cov_node
        """
        mark1 = OmegaMarking(np.array([1, 2, 3, float("inf")]))
        with self.assertRaises(Exception):
            CovNode(1, 2, 3)
        with self.assertRaises(Exception):
            CovNode(mark1, 8)

        node1 = CovNode(mark1, mark1.get_dim())

        mark_false = OmegaMarking(np.array([1, 2, 3, float("inf"), 5]))
        with self.assertRaises(Exception):
            CovNode(mark_false, 5, 0, node1)

        mark2 = OmegaMarking(np.array([1, 2, 5, float("inf")]))
        node2 = CovNode(mark2, mark2.get_dim(), node1._depth, node1)
        mark0 = OmegaMarking(np.array([0, 2, 5, 0]))
        node0 = CovNode(mark0, mark0.get_dim())

        node1.change_parent(node0)

        trans = [OmegaTransition(np.array([1, 2, 3, 5]),
                                 np.array([1, 4, 3, -5])),
                 OmegaTransition(np.array([1, float("inf"), 3, 5]),
                                 np.array([2, 3, 3, -5])),
                 OmegaTransition(np.array([1, 1, 2, 5]),
                                 np.array([5, 5, float("inf"), 8]))]

        node2.successors(trans)
        self.assertEqual(len(node2.get_children()), 2)
        node1.delete_child(node2)
        self.assertEqual(len(node1.get_children()), 0)

    def test_cov_tree_create_insert_delete(self):
        petri = PetriNet(4)
        mark1 = OmegaMarking(np.array([1, 3, 6, float("inf")]))
        node1 = CovNode(mark1, mark1.get_dim())
        mark2 = OmegaMarking(np.array([1, 3, 5, float("inf")]))
        node2 = CovNode(mark2, mark2.get_dim(), node1._depth, node1)

        tr = CovTree(petri, mark1)
        mark0 = OmegaMarking(np.array([0, 2, 5, 0]))
        node0 = CovNode(mark0, mark0.get_dim(), tr.get_root())
        node1.change_parent(node0)
        tr.add_node(node0)
        tr.add_node(node1)
        tr.add_node(node2)
        #         print(node2.GetMark()._marking)
        self.assertEqual(len(tr.get_vertices()), 4)
        tr.delete_node(node2)
        self.assertEqual(len(tr.get_vertices()), 3)
        tr.delete_node(node0)
        self.assertEqual(len(tr.get_vertices()), 1)

    def test_cov_tree_accelerate(self):
        petri = PetriNet(4)
        mark1 = OmegaMarking(np.array([1, 3, 6, float("inf")]))
        node1 = CovNode(mark1, mark1.get_dim())
        mark2 = OmegaMarking(np.array([1, 3, 5, float("inf")]))
        node2 = CovNode(mark2, mark2.get_dim(), node1._depth, node1)

        tr = CovTree(petri, mark1)
        mark0 = OmegaMarking(np.array([0, 2, 5, 0]))
        node0 = CovNode(mark0, mark0.get_dim(), tr.get_root())
        node1.change_parent(node0)
        tr.add_node(node0)
        tr.add_node(node1)
        tr.add_node(node2)
        tr._accelerate(node2, True)
        self.assertTrue(len(tr._accelerations) == 1)

    def test_Alain_2005(self):
        petri = PetriNet(7)

        # Adding transitoins:
        petri.add_transition(OmegaTransition(
            np.array([1, 0, 0, 0, 0, 0, 0]),
            np.array([-1, 1, 0, 0, 0, 0, 0])))
        petri.add_transition(OmegaTransition(
            np.array([1, 0, 0, 0, 0, 0, 0]),
            np.array([-1, 0, 0, 0, 0, 0, 1])))
        petri.add_transition(OmegaTransition(
            np.array([1, 0, 0, 0, 0, 0, 0]),
            np.array([-1, 0, 0, 0, 0, 1, 0])))
        petri.add_transition(OmegaTransition(
            np.array([0, 0, 0, 0, 0, 1, 0]),
            np.array([0, 0, 0, 1, 2, -1, 0])))
        petri.add_transition(OmegaTransition(
            np.array([0, 1, 0, 0, 0, 0, 0]),
            np.array([0, -1, 1, 0, 0, 0, 0])))
        petri.add_transition(OmegaTransition(
            np.array([0, 0, 1, 0, 0, 0, 0]),
            np.array([0, 0, -1, 1, 0, 0, 0])))
        petri.add_transition(OmegaTransition(
            np.array([0, 0, 0, 1, 0, 0, 0]),
            np.array([0, 0, 1, -1, 1, 0, 0])))
        petri.add_transition(OmegaTransition(
            np.array([0, 0, 0, 0, 0, 0, 1]),
            np.array([0, 1, 0, 0, 1, 0, -1])))

        # Marking the net:
        petri.mark_the_petri_net(OmegaMarking(np.array([1, 0, 0, 0, 0, 0, 0])))

        # Initializing the tree:
        cov_tree = CovTreeHash(petri, petri.get_mark())

        anti_chain = cov_tree.generate_cov_tree()
        self.assertEqual(len(anti_chain), 6)

        # for i in anti_chain:
        #     print (i.GetMark()._marking)

    def test_banana_land(self):
        petri = PetriNet(6)

        # Adding transitions:
        petri.add_transition(OmegaTransition(
            np.array([1, 0, 0, 0, 0, 0]),
            np.array([-1, 1, 1, 0, 0, 0])))
        petri.add_transition(OmegaTransition(
            np.array([1, 0, 0, 0, 0, 0]),
            np.array([-1, 1, 0, 1, 0, 0])))
        petri.add_transition(OmegaTransition(
            np.array([1, 0, 0, 0, 0, 0]),
            np.array([-1, 0, 1, 1, 0, 0])))
        petri.add_transition(OmegaTransition(
            np.array([0, 1, 0, 0, 0, 0]),
            np.array([0, 0, 0, 0, 1, 0])))
        petri.add_transition(OmegaTransition(
            np.array([0, 0, 0, 1, 0, 0]),
            np.array([0, 0, 0, -1, 0, 1])))
        petri.add_transition(OmegaTransition(
            np.array([0, 0, 1, 0, 1, 0]),
            np.array([0, 0, 0, 0, -1, 1])))

        # Marking the net:
        petri.mark_the_petri_net(OmegaMarking(np.array([1, 0, 0, 0, 0, 0])))

        # Initializing the tree:
        cov_tree = CovTreeHash(petri, petri.get_mark())

        anti_chain = cov_tree.generate_cov_tree(True)

        self.assertEqual(len(anti_chain), 4)

        markings = []
        for node in anti_chain:
            markings.append(node.get_mark())

        self.assertTrue(OmegaMarking(np.array([1, 0, 0, 0, 0, 0])) in markings)
        self.assertTrue(OmegaMarking(np.array([0, 1, 1, 0, float("inf"), float("inf")])) in markings)
        self.assertTrue(OmegaMarking(np.array([0, 1, 0, 1, float("inf"), 0])) in markings)
        self.assertTrue(OmegaMarking(np.array([0, 0, 1, 1, 0, 0])) in markings)

        self.assertTrue(len(cov_tree._accelerations) == 2)

    def test_mesh_2x2(self):
        petri = load_petri_net_from_spec("benchmarks/mesh2x2.spec")
        cov = CovTreeHash(petri, petri.get_mark().get_marking())
        cov.check_for_correctness = False
        anti_chain = cov.generate_cov_tree()
        self.assertEqual(len(anti_chain), 256)

    def test_short_comparison_to_mp(self):
        dir_test = "tests/short_compare_to_MP/"
        for folder in os.walk("tests/short_compare_to_MP"):
            for file in os.listdir(folder[0]):
                if not file.endswith(".spec"):
                    continue
                print(file)
                petri = load_petri_net_from_spec(dir_test + file)
                cov = CovTreeHashTest(petri, petri.get_mark())
                cov.check_for_correctness = True
                cov.use_of_acc = True
                mcs = cov.generate_cov_tree()
                mp_markings = load_marking_from_mp(dir_test + file.replace('.spec', '_marks'))
                for node in mcs:
                    ok = False
                    for mark in mp_markings:
                        if all(node.marking == mark):
                            ok = True
                            break
                    if not ok:
                        raise Exception("there is a inconsistency with the MCS from MP in + %s" % file)



    # def long_test_compare_to_mp_reasults(self):
    #     dir_test = "tests/"
    #     for folder in os.walk("tests"):
    #         for file in os.listdir(folder[0]):
    #             if not file.endswith(".spec"):
    #                 continue
    #             petri = load_petri_net_from_spec(dir_test+file)
    #             cov = CovTreeHash(petri, petri.get_mark().get_marking())
    #             cov.check_for_correctness = True
    #             cov.use_of_acc = True
    #             mcs = cov.generate_cov_tree()
    #             mp_markings = load_marking_from_mp(dir_test+file.replace('.spec', '_marks'))
    #             print(file)
    #             for node in mcs:
    #                 ok = False
    #
    #                 for mark in mp_markings:
    #                     if all(node.marking == mark):
    #                         ok = True
    #                 if not ok:
    #                     raise Exception("there is a inconsistency with the MCS from MP in + %s" %file)



if __name__ == "__main__":
    # unittest.main()
    cProfile.run('unittest.main()')

