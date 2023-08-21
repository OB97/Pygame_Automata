import pygame
import sys
from Objects import Automaton


class GameBoard(object):

    ### INITIALIZE ###

    # initialize board
    def __init__(self):

        pygame.display.set_caption("Game of Life - Created by Alex")
        self.cell_status1_colour = 0, 0, 0
        self.cell_status2_colour = 100, 100, 100
        self.cell_status3_colour = 255, 255, 255
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
        print(self.active_grid)

        self.paused = True
        self.game_over = False

    # Initialize Grid
    # used during gameboard init
    def init_grids(self):
        self.active_grid = [[Automaton.Automaton() for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.inactive_grid = self.active_grid

    ### GAME ACTIONS ###

    # Update Cells
    # used in main loop, iterate over grid and perform operations on objs contained in cells
    def update_grid(self):
        for row in range(self.num_rows - 1):
            for col in range(self.num_cols - 1):
                obj = self.inactive_grid[row][col]
                n = obj.getNeighbours(self.inactive_grid, row, col)
                if obj.getStatus() == 1:
                    if n == 2:
                        obj.setStatus(3)
                elif obj.getStatus() == 2:
                    obj.setStatus(1)
                elif obj.getStatus() == 3:
                    if n == 2 or n == 3:
                        obj.setStatus(2)

    # Draw Grid
    # used during main loop - missing other uses?
    def draw_grid(self):
        self.clear_screen()
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                obj = self.active_grid[row][col]
                colour = self.get_colour(obj.getStatus())
                posn = (int(col * self.cell_size + self.cell_size / 2),
                        int(row * self.cell_size + self.cell_size / 2))
                pygame.draw.circle(self.screen, colour, posn, int(self.cell_size / 2), 0)
        pygame.display.flip()

    # Handle Events
    # used in main loop, check for event before performing operations on cells
    def handle_events(self):
        for event in pygame.event.get():
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

    ### UTILITY ###

    # Get Automaton Colour
    # used in drawGrid, pass in the obj status value return respective colour of cell
    def get_colour(self, inp):
        if inp == 1:
            return self.cell_status1_colour
        elif inp == 2:
            return self.cell_status2_colour
        else:
            return self.cell_status3_colour

    # Clear Screen
    # used before drawing screen + gameboard init
    def clear_screen(self):
        self.screen.fill(self.cell_status1_colour)

    def swap_grid(self):
        self.active_grid, self.inactive_grid = self.inactive_grid, self.active_grid
