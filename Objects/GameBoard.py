import numpy as np

# GameBoard Object: stores the board state, with each cell in its grid either empty or containing an automaton
### Grid, Automatons, Update


class GameBoard(object):

    def __init__(self):
        self.cellGrid = np.zeros((60, 80))
        self.COLOR_BG = (10, 10, 10)
        self.COLOR_GRID = (40, 40, 40)
        self.COLOR_DIE_NEXT = (170, 170, 170)
        self.COLOR_ALIVE_NEXT = (255, 255, 255)

    def getGrid(self):
        return self.cellGrid

    def setGrid(self, inp):
        self.cellGrid = inp

    def updateGame(self, screen, size):
        return self.cellGrid
