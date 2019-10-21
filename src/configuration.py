"""
Created on Jul 8, 2019

@author: ikhmelnitsky
"""


class Configuration(object):

    def __init__(self):
        pass

    def __eq__(self, other):
        raise NotImplementedError()

    def __ne__(self, other):
        raise NotImplementedError()

    def __gt__(self, other):
        raise NotImplementedError()

    def __ge__(self, other):
        raise NotImplementedError()

    def __lt__(self, other):
        raise NotImplementedError()

    def __le__(self, other):
        raise NotImplementedError()

    def __hash__(self):
        raise NotImplementedError()
