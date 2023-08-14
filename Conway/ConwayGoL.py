# Implementation of Conway's Game of Life
# Alex O'Brien
import pygame
from Objects import GameBoard


# Main Function
def run(game):
    pygame.init()
    pygame.display.set_caption("Game of Life - Created by ")
    pygame.display.flip()

    while True:
        if game.game_over:
            return

        game.handle_events()

        if game.paused:
            continue

        game.update_cells()
        game.draw_grid()
        game.FPSCLOCK.tick(5)


if __name__ == '__main__':
    g = GameBoard.GameBoard()
    run(g)
