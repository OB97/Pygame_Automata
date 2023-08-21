import pygame
import sys
from Objects import Automaton


class GameBoard(object):

    # INITIALIZE #

    # initialize board
    def __init__(self):

        pygame.display.set_caption("Game of Life - Created by Alex")
        self.cell_dead_colour = 0, 0, 0
        self.cell_alive_colour = 255, 255, 255
        self.grid_size = width, height = 1280, 720
        self.cell_size = 10

        self.FPSCLOCK = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.grid_size)
        self.clear_screen()

        self.num_cols = int(width / self.cell_size)
        self.num_rows = int(height / self.cell_size)

        self.active_grid = []
        self.inactive_grid = []
        self.init_grids()

        self.paused = True
        self.game_over = False

    # Initialize Grid
    # used during gameboard init
    def init_grids(self):
        return

    # GAME ACTIONS #

    # Draw Grid
    # used during main loop - missing other uses?
    def draw_grid(self):
        return

    # Update Cells
    # used in main loop, iterate over grid and perform operations on objs contained in cells
    def update_grid(self):
        return

    # Handle Events
    # used in main loop, check for event before performing operations on cells
    def handle_events(self):
        return

    # UTILITY #

    # Get Automaton Colour
    # used in drawGrid, pass in the obj status value return respective colour of cell
    def get_colour(self, inp):
        return

    # Clear Screen
    # used before drawing screen + gameboard init
    def clear_screen(self):
        return
