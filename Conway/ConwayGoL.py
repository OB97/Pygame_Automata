# Implementation of Conway's Game of Life
# Alex O'Brien
import pygame
from Objects import GameBoard


# Main Function
def run(game):
    pygame.init()
    pygame.display.flip()

    while True:
        if game.game_over:
            return

        game.handle_events()

        if game.paused:
            continue

        game.update_grid()
        game.draw_grid()
        game.swap_grid()
        game.FPSCLOCK.tick(30)


if __name__ == '__main__':
    g = GameBoard.GameBoard()
    run(g)
