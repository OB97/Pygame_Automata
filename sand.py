# Implementation of Falling Sand
# Alex O'Brien

import time
import pygame
import numpy as np

# Set Colour Values
COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_DIE_NEXT = (102, 102, 0)
COLOR_ALIVE_NEXT = (255, 255, 0)


# Cell Update Function
def update(screen, cells, size, with_progress=False):
    # 'Updated cells' stores the result of operations performed on 'cells' to apply to the display
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    # Iterate over 2D 'cells' array
    for row, col in np.ndindex(cells.shape):
        # 'color' is BG if the cell is empty, or else it starts to change
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE_NEXT

        # If current cell is filled, check space underneath and update values
        if cells[row, col] == 1:
            if row < len(cells) - 1:
                if cells[row+1, col] == 0:
                    updated_cells[row, col] = 0
                    updated_cells[row+1, col] = 1
                    color = COLOR_DIE_NEXT
                else:
                    updated_cells[row, col] = 1
                    color = COLOR_ALIVE_NEXT
            else:
                updated_cells[row, col] = 1

        # Draw the rectangle?
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
