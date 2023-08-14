import numpy as np


class Automaton(object):

    def __init__(self):
        self.status = 0

    def __repr__(self):
        return "Automaton Object"

    def getStatus(self):
        return self.status

    def switchStatus(self):
        if self.status == 0:
            self.status = 1
        else:
            self.status = 0


if __name__ == "__main__":
    a = Automaton()
