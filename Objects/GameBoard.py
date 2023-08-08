import numpy as np
import pygame
import time


class GameBoard:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.cellGrid = np.zeros((60, 80))
        self.withProgress = False

    def getScreen(self):
        return self.screen

    def getGrid(self):
        return self.cellGrid

    def fillGrid(self, inColour):
        return self.screen.fill(inColour)

    def updateGame(self, size):
        return self
