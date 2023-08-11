import numpy as np
import pygame
import random
import sys

# GameBoard Object

grid_size = width, height = 1280, 720
cell_size = 10
color_dead = 0, 0, 0
color_alive = 255, 255, 255
fps_max = 60


class GameBoard(object):

    # initialize board
    def __init__(self):

        self.FPSCLOCK = pygame.time.Clock()
        self.screen = pygame.display.set_mode(grid_size)
        self.clear_screen()

        self.last_update_completed = 0
        self.active_grid = 0
        self.num_cols = int(width / cell_size)
        self.num_rows = int(height / cell_size)
        self.grids = []
        self.init_grids()
        self.set_random_grid()
        self.paused = True
        self.game_over = False

    # initialize grid
    def init_grids(self):
        # sub-function
        def create_grid():
            rows = []
            for row_num in range(self.num_rows):
                list_of_columns = [0] * self.num_cols
                rows.append(list_of_columns)
            return rows

        self.grids.append(create_grid())
        self.grids.append(create_grid())
        self.active_grid = 0

    def set_random_grid(self, value=None, grid=0):
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                if value is None:
                    cell_value = random.choice([0, 1])
                else:
                    cell_value = value
                self.grids[grid][r][c] = cell_value

    def draw_grid(self):
        # reset grid
        self.clear_screen()
        # iterate over columns
        for col in range(self.num_cols):
            # iterate over rows
            for row in range(self.num_rows):
                # if cell is alive
                if self.grids[self.active_grid][row][col] == 1:
                    color = color_alive
                else:
                    color = color_dead

                posn = (int(col * cell_size + cell_size / 2),
                        int(row * cell_size + cell_size / 2))
                pygame.draw.circle(self.screen, color, posn, int(cell_size / 2), 0)
        pygame.display.flip()

    def clear_screen(self):
        self.screen.fill(color_dead)

    def get_cell(self, row, col):
        return self.grids[self.active_grid][row][col]

    def check_cell_neighbors(self, row_index, col_index):
        num_alive_neighbors = 0
        num_alive_neighbors += self.get_cell(row_index - 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index)
        num_alive_neighbors += self.get_cell(row_index - 1, col_index + 1)
        num_alive_neighbors += self.get_cell(row_index, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index, col_index + 1)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index - 1)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index)
        num_alive_neighbors += self.get_cell(row_index + 1, col_index + 1)

        # Rules
        # 1 Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        # 2 Any live cell with two or three live neighbours lives on to the next generation.
        # 3 Any live cell with more than three live neighbours dies, as if by overpopulation.
        # 4 Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

        if self.grids[self.active_grid][row_index][col_index] == 1:
            if num_alive_neighbors > 3:
                return 0
            if num_alive_neighbors < 2:
                return 0
            if num_alive_neighbors == 2 or num_alive_neighbors == 3:
                return 1
        elif self.grids[self.active_grid][row_index][col_index] == 0:
            if num_alive_neighbors == 3:
                return 1
        return self.grids[self.active_grid][row_index][col_index]

    def update_generation(self):
        self.set_random_grid(0, self.inactive_grid())
        for r in range(self.num_rows - 1):
            for c in range(self.num_cols - 1):
                next_gen_state = self.check_cell_neighbors(r, c)
                self.grids[self.inactive_grid()][r][
                    c] = next_gen_state
        self.active_grid = self.inactive_grid()

    def inactive_grid(self):
        return (self.active_grid + 1) % 2

    def handle_events(self):
        for event in pygame.event.get():
            if self.paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mousepos_x, mousepos_y = event.pos
                        r, c = ((mousepos_x - cell_size / 2) // cell_size,
                                (mousepos_y - cell_size / 2) // cell_size)
                        print(event.pos, '->', (r, c))
                        for col in range(self.num_cols):
                            for row in range(self.num_rows):
                                if self.grids[self.active_grid][col][row] == 1:
                                    color = color_dead
                                elif self.grids[self.active_grid][col][row] == 0:
                                    color = 255, 0, 255
                                else:
                                    color = color_dead

                        posn = (int(r * cell_size + cell_size / 2),
                                int(c * cell_size + cell_size / 2))
                        print(posn)
                        pygame.draw.circle(self.screen, color, posn, int(cell_size / 2), 0)
                pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.unicode == 's':
                    if self.paused:
                        self.paused = False
                        print("live")
                    else:
                        self.paused = True
                        print("paused")
                elif event.unicode == 'r':
                    print("randomizing the grid")
                    self.active_grid = 0
                    self.set_random_grid(None, self.active_grid)
                    self.set_random_grid(0, self.inactive_grid())
                    self.draw_grid()
                # Quit
                elif event.unicode == 'q':
                    print("Quitting the grid")
                    self.game_over = True

            # if event is keypress of "s" then pause the loop/game.
            # if event is keypress "r" then randomize grid
            # if event is keypress of "q"then quit
            if event.type == pygame.QUIT:
                sys.exit()

