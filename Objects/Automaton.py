import numpy as np


class Automaton(object):

    def __init__(self, size, location):
        self.size = size
        self.location = location
        self.status = 0
        self.colour = None
        self.COLOUR_DIE = (170, 170, 170)
        self.COLOUR_ALIVE = (255, 255, 255)

    def getSize(self):
        return self.size

    def getLocation(self):
        return self.location

    def nextMove(self):
        return self

    def allMoves(self):
        return self

    def getStatus(self):
        return self.status

    def setStatus(self, inp):
        self.status = inp

    def getColour(self):
        if self.status == 0:
            return self.COLOUR_DIE
        else:
            return self.COLOUR_ALIVE

    def setColour(self, inp):
        self.colour = inp
