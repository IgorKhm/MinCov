"""
Created on Jul 8, 2019

@author: ikhmelnitsky
"""
import numpy as np

from omega_transition import OmegaTransition


class PetriNet:

    def __init__(self, dim):
        assert (dim > 0), \
            "dimension has to be grater then 0"
        assert (isinstance(dim, int)), \
            "dimension can only be an integer"

        self._dim = dim
        self._transitions = []
        self._marking = None
        self._places = range(0, dim)

    def mark_the_petri_net(self, mark: np.array):
        assert (len(mark) == self._dim), \
            "The dim has to be the same for the marking and the net"
        self._marking = mark

    def add_transition(self, tran: OmegaTransition):
        assert (tran.get_dim() == self._dim)
        self._transitions.append(tran)

    def get_transitions(self):
        return self._transitions

    def get_mark(self):
        return self._marking

    def get_places(self):
        return self._places

    def get_dim(self):
        return self._dim

    def order_transitions(self):
        self._transitions = sorted(self._transitions, key=lambda x: sum(x.get_incidence()) - sum(x.get_pre()) )
        # self._transitions.reverse()
        return
