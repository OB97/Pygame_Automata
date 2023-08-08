# Implementation of Conway's Game of Life
# Alex O'Brien

import time
import pygame
import numpy as np
from Objects import GameBoard

COLOUR_BG = GameBoard.GameBoard().COLOR_BG
COLOUR_GRID = GameBoard.GameBoard().COLOR_ALIVE_NEXT


# Main Function
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill(COLOUR_BG)

    gb = GameBoard.GameBoard()
    gb.updateGame(screen, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == '__main__':
    main()
