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
        self.cell_change_colour = 155, 0, 0
        self.cell_active_colour = 150, 150, 150
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
    # used during gameboard init, creates 2 empty grids
    def init_grids(self):
        self.active_grid = [[Automaton.Automaton(self.genStatus()) for _ in range(self.num_cols)] for _ in
                            range(self.num_rows)]
        self.inactive_grid = self.active_grid

    ### GAME ACTIONS ###

    # Update Cells
    # used in main loop, where Automaton values change
    def update_grid(self):
        for row in range(self.num_rows - 1):
            for col in range(self.num_cols - 1):
                obj = self.active_grid[row][col]
                n = self.getNeighbours(row, col)
                # if dead
                if obj.getStatus() == 1:
                    if n == 2 or n == 3:
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
        for row in range(self.num_rows - 1):
            for col in range(self.num_cols - 1):
                obj = self.active_grid[row][col]
                colour = self.get_colour(obj.getStatus())
                posn = (int(col * self.cell_size + self.cell_size / 2),
                        int(row * self.cell_size + self.cell_size / 2))
                pygame.draw.circle(self.screen, colour, posn, int(self.cell_size / 2), 0)
        pygame.display.flip()
        self.colourShift()

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
                        self.active_grid[int(r)][int(c)].setStatus(4)
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

    def colourShift(self):

        rActive = self.cell_active_colour[0]
        bActive = self.cell_active_colour[0]
        gActive = self.cell_active_colour[2]
        rInactive = self.cell_inactive_colour[0]
        bInactive = self.cell_inactive_colour[1]
        gInactive = self.cell_inactive_colour[2]
        rChanging = self.cell_change_colour[0]
        bChanging = self.cell_change_colour[1]
        gChanging = self.cell_change_colour[2]

        lst1 = [rActive, bActive, gActive, rInactive, bInactive, gInactive, rChanging, bChanging, gChanging]
        lst2 = [rInactive, bInactive, gInactive]
        lst3 = [rChanging, bChanging, gChanging]

        for val1 in range(len(lst1)):
            if lst1[val1] >= 100:
                lst1[val1] = random.randint(10, 80)
            else:
                lst1[val1] += 1

        for val2 in range(len(lst2)):
            if lst2[val2] >= 250:
                lst2[val2] = random.randint(225, 230)
            else:
                lst2[val2] += 1

        for val3 in range(len(lst3)):
            if lst3[val3] >= 75:
                lst3[val3] = random.randint(100, 200)
            else:
                lst3[val3] += 1

        self.cell_active_colour = lst1[0], lst1[1], lst1[2]
        self.cell_inactive_colour = lst2[0], lst2[1], lst2[2]
        self.cell_change_colour = lst3[0], lst3[1], lst3[2]

    @staticmethod
    def genStatus():
        return random.choice([1, 4])
