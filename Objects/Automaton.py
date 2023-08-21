import random


class Automaton(object):

    def __init__(self):
        self.status = self.genStatus()

    def __repr__(self):
        return "Automaton Object - Value: " + str(self.getStatus())

    def getStatus(self):
        return self.status

    @staticmethod
    def genStatus():
        return random.randint(0, 1)

    def switchStatus(self):
        if self.status == 0:
            self.status = 1
        else:
            self.status = 0

    @staticmethod
    def getNeighbours(grid, row, col):
        count = 0
        n1 = grid[row + 1][col]
        n2 = grid[row - 1][col]
        n3 = grid[row][col + 1]
        n4 = grid[row][col - 1]

        if n1.getStatus() == 1:
            count += 1
        if n2.getStatus() == 1:
            count += 1
        if n3.getStatus() == 1:
            count += 1
        if n4.getStatus() == 1:
            count += 1

        return count
