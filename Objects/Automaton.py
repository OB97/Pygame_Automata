import random


class Automaton(object):

    def __init__(self, inp):
        self.status = inp

    def __repr__(self):
        return "Automaton Object - Value: " + str(self.getStatus())

    def getStatus(self):
        return self.status

    def setStatus(self, inp):
        self.status = inp



