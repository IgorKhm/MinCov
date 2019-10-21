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

import numpy as np


class OmegaTransition:

    def __init__(self, pre: np.array, incidence: np.array):
        # make sure that pre and "post" are of the same length
        assert (len(pre) == len(incidence)), "length are wrong"
        assert (all(np.greater_equal(pre + incidence, np.zeros(len(pre))))), \
            "incidence + pre must be greater then 0"

        self._dim = len(pre)
        self._pre = pre
        self._incidence = incidence
        if (self._dim / 1 > np.count_nonzero(incidence)) & (self._dim / 10 > np.count_nonzero(pre)):
            self._short_prese = True
            self._pre_short = [(i, value) for i, value in zip(range(self._dim), pre) if pre[i] != 0]
            self._incidence_short = [(i, value) for i, value in zip(range(self._dim), incidence) if incidence[i] != 0]
        else:
            self._short_prese = False

    def __eq__(self, other):
        return all((self._pre == other._pre) &
                   (self._incidence == other._incidence))

    def __ne__(self, other):
        return any((self._pre != other._pre) |
                   (self._incidence != other._incidence))

    def __gt__(self, other):
        return all((self._pre < other._pre) &
                   (self._incidence > other._incidence))

    def __ge__(self, other):
        return all((self._pre <= other._pre) &
                   (self._incidence >= other._incidence))

    def __lt__(self, other):
        return other > self

    def __le__(self, other):
        return other >= self

    def get_pre(self):
        return self._pre

    def get_incidence(self):
        return self._incidence

    def get_dim(self):
        return self._dim

    def apply_on_marking(self, marking: np.array):
        new_marking = np.copy(marking)
        if self._short_prese:
            for (i, value) in self._incidence_short:
                new_marking[i] = marking[i] + value
        else:
            new_marking = new_marking + self._incidence
        return new_marking

    def is_fireable_from(self, marking: np.array):
        if self._short_prese:
            for i, value in self._pre_short:
                if marking[i] < value:
                    return False
            return True
        else:
            return not any(marking < self._pre)
