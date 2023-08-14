import numpy as np
import pygame
import random
import sys
from Objects import Automaton


class GameBoard(object):

    # initialize board
    def __init__(self):

        self.grid_empty_colour = 0, 0, 0
        self.cell_dead_colour = 170, 170, 170
        self.cell_alive_colour = 255, 255, 255
        self.grid_size = width, height = 1280, 720
        self.cell_size = 10

        self.FPSCLOCK = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.grid_size)
        self.clear_screen()

        self.num_cols = int(width / self.cell_size)
        self.num_rows = int(height / self.cell_size)
        self.grid = []
        self.init_grid()
        self.paused = True
        self.game_over = False

    # initialize grid
    def init_grid(self):
        self.grid = [[Automaton.Automaton()] * self.num_cols] * self.num_rows
        print(self.grid)

    def draw_grid(self):
        self.clear_screen()
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                posn = (int(col * self.cell_size + self.cell_size / 2),
                        int(row * self.cell_size + self.cell_size / 2))
                pygame.draw.circle(self.screen, self.getColour(self.grid[row][col]), posn, int(self.cell_size / 2), 0)
        pygame.display.flip()

    def clear_screen(self):
        self.screen.fill(self.grid_empty_colour)

    def getColour(self, inp):
        status = inp.getStatus()
        if status == 1:
            return self.cell_alive_colour
        else:
            return self.cell_dead_colour

    def update_cells(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col].switchStatus())

    def handle_events(self):
        for event in pygame.event.get():
            # If Paused check for input
            if self.paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mousepos_x, mousepos_y = event.pos
                        r, c = ((mousepos_x - self.cell_size / 2) // self.cell_size,
                                (mousepos_y - self.cell_size / 2) // self.cell_size)
                        print(event.pos, '->', (r, c))
                        posn = (int(r * self.cell_size + self.cell_size / 2),
                                int(c * self.cell_size + self.cell_size / 2))
                        print(posn)
                        pygame.draw.circle(self.screen, self.cell_alive_colour, posn, int(self.cell_size / 2), 0)
                pygame.display.flip()
            # Check for event
            if event.type == pygame.KEYDOWN:
                if event.unicode == 's':
                    if self.paused:
                        self.paused = False
                        print("Live")
                    else:
                        self.paused = True
                        print("Paused")
                # Reset
                elif event.unicode == 'r':
                    print("Resetting Grid")
                    self.__init__()
                # Quit Key
                elif event.unicode == 'q':
                    print("Quitting Grid")
                    self.game_over = True
            # Quit Button
            if event.type == pygame.QUIT:
                sys.exit()
