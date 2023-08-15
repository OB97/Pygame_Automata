# Implementation of Conway's Game of Life
# Alex O'Brien
import pygame
from Objects import GameBoard


# Main Function
def run(game):
    pygame.init()
    pygame.display.set_caption("Game of Life - Created by ")
    pygame.display.flip()
    x = 0

    while x < 5:
        if game.game_over:
            return

        game.handle_events()

        if game.paused:
            continue

        print("M-Update Grid: ")
        game.update_grid()
        print("M-Draw Grid: ")
        game.draw_grid()
        print("M-Tick: ")
        game.FPSCLOCK.tick(20)
        x += 1


if __name__ == '__main__':
    g = GameBoard.GameBoard()
    run(g)
