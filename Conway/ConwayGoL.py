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
        game.active_grid, game.inactive_grid = game.inactive_grid, game.active_grid  # game.switchGrid()?
        game.FPSCLOCK.tick(10)


if __name__ == '__main__':
    g = GameBoard.GameBoard()
    run(g)
