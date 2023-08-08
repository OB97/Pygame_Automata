import numpy as np
import pygame
import time


class GameBoard(object):

    def __init__(self, withProgress):
        self.screen = pygame.display.set_mode((800, 600))
        self.cellGrid = np.zeros((60, 80))
        self.withProgress = withProgress

    def getScreen(self):
        return self.screen

    def getGrid(self):
        return self.cellGrid

    def switchState(self):
        if not self.withProgress:
            self.withProgress = True
        else:
            self.withProgress = False

    def updateGame(self, size):
        return self

    def fillGrid(self, inColour):
        self.screen.fill(inColour)
