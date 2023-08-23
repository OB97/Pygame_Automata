import random


class Automaton(object):

    def __init__(self, instat):
        self.status = instat

    def __repr__(self):
        return "Automaton Object - Value: " + str(self.getStatus())

    def getStatus(self):
        return self.status

    def setStatus(self, inp):
        self.status = inp

