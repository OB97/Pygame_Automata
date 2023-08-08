import numpy as np


class Automaton(object):

    def __init__(self, size, identifier, status):
        self.size = size
        self.identifier = identifier
        self.status = status

    def getSize(self):
        return self.size

    def getID(self):
        return self.identifier

    def nextMove(self):
        return self

    def allMoves(self):
        return
