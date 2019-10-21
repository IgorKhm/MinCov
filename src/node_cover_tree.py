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

from copy import deepcopy

import numpy as np


from omega_transition import OmegaTransition


class CovNode(object):

    def __init__(self, mark: np.array, dim, depth=0, parent=None):
        """
        Constructor
        """
        assert (len(mark) == dim), \
            "The dimension of the node and its marking has to be the same"

        self._depth = depth
        self.marking = mark
        self._dim = dim
        self._children = []
        self._tranFromParent = []

        self.num_of_omegas = np.count_nonzero(mark == float("inf"))
        tmp = np.where(mark != float("inf"), mark, 0)
        self.sum_of_not_omega = np.sum(tmp)

        self._parent = None
        if parent is not None:
            assert (dim == parent.get_dim()), \
                "The dimension of the node and its parent has to be the same"
        self.change_parent(parent)
        self.trans_to_fire = 0

    def get_dim(self):
        return self._dim

    def set_marking(self, mark: np.array):
        self.marking = mark
        self.num_of_omegas = np.count_nonzero(mark == float("inf"))
        tmp = np.where(mark != float("inf"), mark, 0)
        self.sum_of_not_omega = np.sum(tmp)

    def get_parent(self):
        return self._parent

    def get_children(self):
        return self._children

    def change_parent(self, parent):
        assert ((isinstance(parent, CovNode)) | (parent is None)), \
            "Parents have to be covNodes"
        if parent is not None:
            assert (self._dim == parent.get_dim()), \
                "The dimension of the node and its parent has to be the same"

        if self._parent is not None:
            self._parent.delete_child(self)
        self._parent = parent
        if parent is not None:
            if self not in parent.get_children():
                parent.add_child(self)

    def successors(self, trans):
        for tran in trans:
            if tran.is_fireable_from(self.marking):
                child_mark = deepcopy(self.marking)
                child = CovNode(child_mark.fire_transition(tran),
                                self._dim, self._depth + 1, self)
                child.add_transition(tran)

        return self._children

    def successors_no_duplicates(self, trans: [OmegaTransition]):
        """
        Creates all the successors of the node according to trans such that their marks are an anti-chain
        """
        for tran in trans:
            if tran.is_fireable_from(self.marking):
                new_marking = tran.apply_on_marking(self.marking)
                child = CovNode(new_marking, self._dim, self._depth + 1, self)
                child.add_transition(tran)

        return self._children

    def single_successor(self, tran: OmegaTransition):
        if tran.is_fireable_from(self.marking):
            child_mark = deepcopy(self.marking)
            child = CovNode(child_mark.fire_transition(tran),
                            self._dim, self._depth + 1, self)
            child.add_transition(tran)
            return child
        return None

    def add_child(self, child):
        self._children.append(child)
        if self != child.get_parent():
            child.change_parent(self)

    def delete_child(self, child):
        self._children.remove(child)

    def add_transition(self, tran: OmegaTransition):
        assert (isinstance(tran, OmegaTransition)), \
            "Parents have to be covNodes"
        self._tranFromParent.append(tran)

    def get_transitions(self):
        return self._tranFromParent

    def __repr__(self):
        rep = "marking: " + str(self.marking) + " \n num of children: "+ str(len(self._children)) + ", depth: "+ str(self._depth)
        return rep

    def __lt__(self, other):
        if self.num_of_omegas > other.num_of_omegas:
            return True
        elif self.sum_of_not_omega > other.sum_of_not_omega:
            return True
        else:
            return self._depth >= other._depth
