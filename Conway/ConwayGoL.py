# Implementation of Conway's Game of Life
# Alex O'Brien

import time
import pygame
import numpy as np
from Objects import GameBoard


# Main Function
#  1. initialize live game
#  2. initialize game loop
#  3. call live update if progress is true
def main():
    # 1.
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    curCells = np.zeros((72, 128))
    game = GameBoard.GameBoard(curCells)
    screen.fill(game.COLOUR_GRID)
    update(screen, size=10, gb=game)
    pygame.display.flip()
    pygame.display.update()
    # 2.
    while True:
        running = game.getProgress()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # KEY PRESS
            elif event.type == pygame.KEYDOWN:
                # PAUSE
                if event.key == pygame.K_SPACE:
                    game.switchProgress()
                    update(screen, size=10, gb=game)  # update game-state
                    pygame.display.update()  # update display
                # RESET
                elif event.key == pygame.K_ESCAPE:
                    if running:
                        game.switchProgress()
                    curCells = np.zeros((60, 80))
                    update(screen, size=10, gb=game)
                    pygame.display.update()
            # FILL CELL
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                curCells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, size=10, gb=game)
                pygame.display.update()
            # fill screen after checking event
            screen.fill(game.COLOUR_GRID)
            # 3.
            if running:
                curCells = update(screen, size=10, gb=game)
                pygame.display.update()
            time.sleep(0.01)


# Live Game Update Function
def update(screen, size, gb):
    cells = gb.getGrid()
    newCells = np.zeros((cells.shape[0], cells.shape[1]))
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1:row + 2, col - 1:col + 2]) - cells[row, col]
        # 'color' is BG if the cell is dead, or else it starts to change
        colour = gb.COLOUR_BG if cells[row, col] == 0 else gb.COLOUR_ALIVE
        # Use 'alive' to see if a cell will die or not
        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if gb.getProgress():
                    colour = gb.COLOUR_DIE
            elif 2 <= alive <= 3:
                newCells[row, col] = 1
                if gb.getProgress():
                    colour = gb.COLOR_ALIVE
        else:
            if alive == 3:
                newCells[row, col] = 1
                if gb.getProgress():
                    colour = gb.COLOUR_ALIVE
        pygame.draw.rect(screen, colour, (col * size, row * size, size - 1, size - 1))
    return newCells


if __name__ == '__main__':
    main()
