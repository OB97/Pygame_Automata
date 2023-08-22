import random


class Automaton(object):

    def __init__(self):
        self.status = self.genStatus()

    def __repr__(self):
        return "Automaton Object - Value: " + str(self.getStatus())

    def getStatus(self):
        return self.status

    def setStatus(self, inp):
        self.status = inp

    @staticmethod
    def genStatus():
        return random.choice([1, 3])
