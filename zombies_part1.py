import random
import time

 # constants for grid dimensions
GRID_WIDTH = 20   
GRID_HEIGHT = 10

# constants for number of zombies an quicksand 
ZOMBIE_COUNT = 4 
QUICKSAND_COUNT = 8

# Set area of text and print title on screen

def initialize_screen():
    # Display the game title 
    print(".........OFFICERS")
    print()


# Print area of the ranch within which you and zombies can move
def get_random_coordinate(limit):
        # generate a random coordinate with a given limit
        return random.randint(1,limit)
    
