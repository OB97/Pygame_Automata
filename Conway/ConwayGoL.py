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

        print("M-Update Grid: ")
        game.update_grid()
        print("M-Draw Grid: ")
        game.draw_grid()
        game.active_grid, game.backup_grid = game.backup_grid, game.active_grid
        print("M-Tick: ")
        game.FPSCLOCK.tick(10)


if __name__ == '__main__':
    g = GameBoard.GameBoard()
    run(g)
