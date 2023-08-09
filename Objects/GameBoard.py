import numpy as np

# GameBoard Object: stores the board state, with each cell in its grid either empty or containing an automaton
### Grid, Automatons, Update


class GameBoard(object):

    def __init__(self, cells):
        self.withProgress = False
        self.cellGrid = cells
        self.COLOUR_BG = (10, 10, 10)
        self.COLOUR_GRID = (40, 40, 40)
        self.COLOUR_DIE = (170, 170, 170)
        self.COLOUR_ALIVE = (255, 255, 255)

    def getProgress(self):
        return self.withProgress

    def switchProgress(self):
        if self.withProgress:
            self.withProgress = False
        elif not self.withProgress:
            self.withProgress = True

    def getGrid(self):
        return self.cellGrid

    def setGrid(self, inp):
        self.cellGrid = inp

    def updateGame(self, screen):
        updatedCells = np.zeros((self.cellGrid.shape[0], self.cellGrid.shape[1]))
        return updatedCells

