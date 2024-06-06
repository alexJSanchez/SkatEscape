import random
import time

# Constants for grid dimensions
GRID_WIDTH = 20
GRID_HEIGHT = 10

# Constants for number of zombies and quicksandd
ZOMBIE_COUNT = 4
QUICKSAND_COUNT = 8

# Set area of text and print title on screen.

def initialize_screen():
    # Display the game title
    print("......ZOMBIES")
    print()

def get_random_coordinate(limit):
      # Generate a random coordinate within the given limit
    return random.randint(1, limit)

# The starting positions of the zombies, which are randomly chosen, are shown.
def create_empty_grid(width, height):
    # Create an empty grid with the given width and height
    grid = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(' ')
        grid.append(row)
    return grid

# The randomly chosen quicksand traps are placed on the screen.
def draw_grid(human, zombies, quicksand):
    # Draw the grid with the current positions of the human, zombies, and quicksand

    # Create an empty grid
    grid = create_empty_grid(GRID_WIDTH, GRID_HEIGHT)

    # Place quicksand in the grid
    for x, y in quicksand:
        grid[y-1][x-1] = '*'
    
    # Place zombies in the grid
    for x, y in zombies:
        if x != 0 and y != 0:
            grid[y-1][x-1] = 'z'
    
    # Place human in the grid
    human_x, human_y = human
    grid[human_y-1][human_x-1] = 'h'

    # Draw the grid with borders
    print("@"*(GRID_WIDTH+2))
    for row in grid:
        print("@" + ''.join(row) + "@")
    print("@"*(GRID_WIDTH+2))

