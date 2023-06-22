# Implementation of Conway's Game of Life
# Alex O'Brien

import time
import pygame
import numpy as np

# Set Colour Values
COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (170, 170, 170)
COLOR_ALIVE_NEXT = (255, 255, 255)


# Cell Update Function
def update(screen, cells, size, with_progress=False):
    # 'Updated cells' stores the result of operations performed on 'cells' to apply to the display
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    # Iterate over 2D 'cells' array
    for row, col in np.ndindex(cells.shape):
        # Count number of neighbours
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        # 'color' is BG if the cell is dead, or else it starts to change
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        # Use 'alive' to see if a cell will die or not
        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE_NEXT

        # Draw the rectangle? What is getting drawn every update?
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells


# Main Function
def main():
    # Initialize screen + game variables
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    cells = np.zeros((60, 80))
    screen.fill(COLOR_GRID)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    # running vs. paused
    running = False

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
                    update(screen, cells, 10)  # update game-state
                    pygame.display.update()  # update display
                # RESET
                elif event.key == pygame.K_ESCAPE:
                    if running:
                        running = not running
                    cells = np.zeros((60, 80))
                    update(screen, cells, 10)
                    pygame.display.update()
            # FILL CELL
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        # Fill screen AFTER checking events
        screen.fill(COLOR_GRID)

        # If not paused, update cells and display
        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        # Tick time, smaller value means more compute cost but smoother movement
        time.sleep(0.01)


if __name__ == '__main__':
    main()
