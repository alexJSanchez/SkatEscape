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
