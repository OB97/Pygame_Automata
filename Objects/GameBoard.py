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
        self.backup_grid = []
        self.init_grids()

        self.paused = True
        self.game_over = False

    # Initialize Grid
    # used during gameboard init
    def init_grids(self):
        self.active_grid = [[Automaton.Automaton() for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.backup_grid = [[Automaton.Automaton() for _ in range(self.num_cols)] for _ in range(self.num_rows)]

    # GAME ACTIONS #

    # Draw Grid
    # used during main loop - missing other uses?
    def draw_grid(self):
        self.clear_screen()
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                obj = self.active_grid[row][col]
                status = obj.getStatus()
                colour = self.get_colour(status)
                posn = (int(col * self.cell_size + self.cell_size / 2),
                        int(row * self.cell_size + self.cell_size / 2))
                pygame.draw.circle(self.screen, colour, posn, int(self.cell_size / 2), 0)

        pygame.display.flip()

    # Update Cells
    # used in main loop, iterate over grid and perform operations on objs contained in cells
    def update_grid(self):
        temp_grid = [[Automaton.Automaton() for _ in range(self.num_cols)] for _ in range(self.num_rows)]

        for row in range(self.num_rows - 1):
            for col in range(self.num_cols - 1):
                obj = self.backup_grid[row][col]
                n = obj.getNeighbours(self.backup_grid, row, col)
                if obj.getStatus() == 1:
                    if n == 2 or n == 3:
                        temp_grid[row][col].switchStatus()
                else:
                    if n == 2:
                        temp_grid[row][col].switchStatus()

        self.backup_grid = temp_grid

    # Handle Events
    # used in main loop, check for event before performing operations on cells
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

    # UTILITY #

    # Get Automaton Colour
    # used in drawGrid, pass in the obj status value return respective colour of cell
    def get_colour(self, inp):
        if inp == 1:
            return self.cell_alive_colour
        else:
            return self.cell_dead_colour

    # Clear Screen
    # used before drawing screen + gameboard init
    def clear_screen(self):
        self.screen.fill(self.cell_dead_colour)
