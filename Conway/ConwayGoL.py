# Implementation of Conway's Game of Life
# Alex O'Brien

import time
import pygame
import numpy as np
from Objects import GameBoard

# Set Colour Values
COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)


# Main Function
def main():
    pygame.init()
    # 1. Init GameBoard Object
    gb = GameBoard.GameBoard(False)
    # 2. Fill screen - COLOUR_GRID
    gb.fillGrid(COLOR_GRID)
    # 3. Update - cell size 1
    gb.updateGame(1)
    # 4. flip display
    pygame.display.flip()
    # 5. update display
    pygame.display.update()

    # Game Loop
    while True:
        for event in pygame.event.get():  # When an event occurs

            # EVENT : QUIT
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # EVENT : KEY PRESS
            elif event.type == pygame.KEYDOWN:

                # PAUSE
                if event.key == pygame.K_SPACE:
                    gb.switchState()
                    gb.updateGame(1)
                    pygame.display.update()

                # RESET
                elif event.key == pygame.K_ESCAPE:
                    # initialize new board
                    gb = GameBoard.GameBoard(False)
                    gb.updateGame(1)
                    pygame.display.update()

            # EVENT : FILL CELL - Need to think of solution
            if pygame.mouse.get_pressed()[0]:
                # pos = pygame.mouse.get_pos()
                # cells[pos[1] // 10, pos[0] // 10] = 1

                gb.updateGame(1)
                pygame.display.update()

        # Fill screen AFTER checking events
        gb.fillGrid(COLOR_GRID)

        # If not paused, update cells and display
        if gb.withProgress:
            # update game + display
            gb.updateGame(1)
            pygame.display.update()

        # Tick time, smaller value means more compute cost but smoother movement
        time.sleep(0.01)


if __name__ == '__main__':
    main()
