import pygame
import random
import sys
from Objects import Automaton


class GameBoard(object):

    ### INITIALIZE ###

    # initialize board
    def __init__(self):
        pygame.display.set_caption("Game of Life - Created by Alex")
        self.cell_inactive_colour = 0, 0, 0
        self.cell_change_colour = 100, 100, 100
        self.cell_active_colour = 255, 255, 255
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
        self.active_grid = [[Automaton.Automaton(self.genStatus()) for _ in range(self.num_cols)] for _ in
                            range(self.num_rows)]
        self.inactive_grid = self.active_grid

    ### GAME ACTIONS ###

    # Update Cells
    # used in main loop, where Automaton values change
    def update_grid(self):
        return

    # Draw Grid
    # used during main loop, draw the grid colours
    def draw_grid(self):
        return

    # Handle Events
    # used in main loop, check for event before performing operations on cells
    def handle_events(self):
        return

    ### UTILITY ###

    # Get Automaton Colour
    # used in drawGrid, pass in the obj status value return respective colour of cell
    def get_colour(self, inp):
        return

    # Clear Screen
    # used before drawing screen + gameboard init
    def clear_screen(self):
        return

    # Swap Active Grid
    # used in main, active grid is what is shown - inactive grid is where operations are performed
    # swap to show differences between active and inactive
    def swap_grid(self):
        return

    # Get Active Neighbours
    # used in update function, returns the number of active neighbour cells
    def getNeighbours(self, row, col):
        return

    @staticmethod
    def genStatus():
        return random.choice([1, 4])
