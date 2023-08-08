import numpy as np
import pygame
import time


class GameBoard:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.cellGrid = np.zeros((60, 80))
        self.withProgress = False

    def getScreen(self):
        return self.screen

    def getGrid(self):
        return self.cellGrid

    def updateGame(self, size):
        return self
