import pygame
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
        self.backup_grid = []
        self.init_grids()

        self.paused = True
        self.game_over = False

    # Initialize Grid
    # used during gameboard init
    def init_grids(self):
        self.active_grid = [[Automaton.Automaton() for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        self.inactive_grid = self.active_grid

    ### GAME ACTIONS ###

    # Update Cells
    # used in main loop, where Automaton values change
    def update_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                obj = self.active_grid[row][col]
                n = self.getNeighbours(row, col)
                # if dead
                if obj.getStatus() == 1:
                    if n == 2:
                        obj.setStatus(3)
                # if dying
                elif obj.getStatus() == 2:
                    obj.setStatus(1)
                # if growing
                elif obj.getStatus() == 3:
                    obj.setStatus(4)
                # if alive
                elif obj.getStatus() == 4:
                    if n == 1 or n == 4:
                        obj.setStatus(2)

    # Draw Grid
    # used during main loop, draw the grid colours
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

            # If Paused check for input
            if self.paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mousepos_x, mousepos_y = event.pos
                        r, c = ((mousepos_x - self.cell_size / 2) // self.cell_size,
                                (mousepos_y - self.cell_size / 2) // self.cell_size)
                        print(r, c)
                        posn = (int(r * self.cell_size + self.cell_size / 2),
                                int(c * self.cell_size + self.cell_size / 2))
                        print(posn)
                        self.active_grid[int(r)][int(c)].setStatus(3)
                        pygame.draw.circle(self.screen, self.cell_active_colour, posn, int(self.cell_size / 2), 0)
                pygame.display.flip()

            # If not Paused look for input
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
            return self.cell_inactive_colour
        elif inp == 2 or inp == 3:
            return self.cell_change_colour
        else:
            return self.cell_active_colour

    # Clear Screen
    # used before drawing screen + gameboard init
    def clear_screen(self):
        self.screen.fill(self.cell_inactive_colour)

    # Swap Active Grid
    # used in main, active grid is what is shown - inactive grid is where operations are performed
    # swap to show differences between active and inactive
    def swap_grid(self):
        self.active_grid, self.inactive_grid = self.inactive_grid, self.active_grid

    # Get Active Neighbours
    # used in update function, returns the number of active neighbour cells
    def getNeighbours(self, row, col):
      
        count = 0
        n1 = self.active_grid[row + 1][col]
        n2 = self.active_grid[row - 1][col]
        n3 = self.active_grid[row][col + 1]
        n4 = self.active_grid[row][col - 1]

        if n1.getStatus() == 4:
            count += 1
        if n2.getStatus() == 4:
            count += 1
        if n3.getStatus() == 4:
            count += 1
        if n4.getStatus() == 4:
            count += 1

        return count

