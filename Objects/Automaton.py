import numpy as np


class Automaton:

    def __init__(self, size, identifier):
        self.size = size
        self.identifier = identifier

    def getSize(self):
        return self.size

    def getCells(self):
        return self.identifier

    def nextMove(self):
        return self
