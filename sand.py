# Implementation of Falling Sand
# Alex O'Brien

import time
import pygame
import numpy as np

# Set Constant Values
COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_SAND = (255, 255, 0)

SCREEN = pygame.display.set_mode((800, 600))
EMPTY_GRID = np.zeros((60, 80))


# Cell Update Function
def update(screen, cells, size, with_progress=False):
    # 'Updated cells' stores the result of operations performed on 'cells' to apply to the display
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    # Iterate over 2D 'cells' array
    for row, col in np.ndindex(cells.shape):
        # 'color' is BG if the cell is empty, or else it starts to change
        color = COLOR_BG if cells[row, col] == 0 else COLOR_SAND

        # If current cell is not empty
        if cells[row, col] == 1:
            # If inside matrix (avoid off-screen click error)
            if row < len(cells) - 1 and col < len(cells[row]) - 1:
                # If cell directly underneath is empty
                if move_status(cells, row, col) == 1:
                    updated_cells[row, col] = 0
                    updated_cells[row + 1, col] = 1
                    color = COLOR_SAND
                # Left diagonal
                elif move_status(cells, row, col) == 2:
                    updated_cells[row, col] = 0
                    updated_cells[row + 1, col - 1] = 1
                    color = COLOR_SAND
                # Right Diagonal
                elif move_status(cells, row, col) == 3:
                    updated_cells[row, col] = 0
                    updated_cells[row + 1, col + 1] = 1
                    color = COLOR_SAND
                # Right AND Left are empty
                else:
                    rand = np.random.rand()
                    # Move left
                    if rand <= 0.49:
                        updated_cells[row, col] = 0
                        updated_cells[row + 1, col - 1] = 1
                        color = COLOR_SAND
                    # Move right
                    else:
                        updated_cells[row, col] = 0
                        updated_cells[row + 1, col + 1] = 1
                        color = COLOR_SAND
                # If no moves available, stay filled
                if move_status(cells, row, col) == 0:
                    updated_cells[row, col] = 1
                    color = COLOR_SAND
            # Outside of matrix
            else:
                if row < len(cells) - 1:  # If col is outside matrix, current cell is left blank
                    updated_cells[row, col] = 0
                elif col < len(cells[row]):  # If row is outside matrix, current cell is filled
                    updated_cells[row, col] = 1

        # Draw the rectangle?
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


# Neighbour Checker
def move_status(cells, row, col):
    result = -1

    # Define neighbours of passed in cell
    under = cells[row + 1, col]
    left = cells[row + 1, col - 1]
    right = cells[row + 1, col + 1]

    # No moves
    if under == 1 and left == 1 and right == 1:
        result = 0
    # Moves
    else:
        # Move down
        if under == 0:
            result = 1
        # Move left or right
        elif left == 0 and right == 0:
            result = 4
        # Move left
        elif left == 0 and right == 1:
            result = 2
        # Move right
        elif left == 1 and right == 0:
            result = 3

    return result


# Main Function
def main():
    # Initialize screen + game variables
    pygame.init()
    cells = EMPTY_GRID
    SCREEN.fill(COLOR_GRID)
    update(SCREEN, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    # running vs. paused
    running = True

    # Game Loop
    while True:
        for event in pygame.event.get():  # When an event occurs
            # QUIT
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # KEY PRESS
            elif event.type == pygame.KEYDOWN:
                # PAUSE
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(SCREEN, cells, 10)  # update game-state
                    pygame.display.update()  # update display
                # RESET
                elif event.key == pygame.K_ESCAPE:
                    if running:
                        running = not running
                    cells = np.zeros((60, 80))
                    update(SCREEN, cells, 10)
                    pygame.display.update()
            # FILL CELL
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()  # Mouse coordinates
                print(pos)  # Debugging
                # If inside screen coordinates
                if pos[0] // 10 < 80 and pos[1] // 10 < 60 and pos[0] > 0 and pos[1] > 0:
                    cells[pos[1] // 10, pos[0] // 10] = 1
                    update(SCREEN, cells, 10)
                    pygame.display.update()

        # Fill screen AFTER checking events
        SCREEN.fill(COLOR_GRID)

        # If not paused, update cells and display
        if running:
            cells = update(SCREEN, cells, 10, with_progress=True)
            pygame.display.update()

        # Tick time
        time.sleep(0.01)


if __name__ == '__main__':
    main()
