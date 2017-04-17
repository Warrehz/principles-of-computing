"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    first_new_line = []
    second_new_line = []

    # appends num if num isn't 0
    for num in line:
        if num != 0:
            first_new_line.append(num)

    # appends 0 if lengths of lines aren't equal
    for num in range(0, len(line)):
        if len(first_new_line) != len(line):
            first_new_line.append(0)

    # adds same numbers together
    for num in range(0, (len(line) - 1)):
        if first_new_line[num] == first_new_line[num + 1]:
            first_new_line[num] += first_new_line[num + 1]
            first_new_line[num + 1] = 0

    # appends num if num isn't 0
    for num in first_new_line:
        if num != 0:
            second_new_line.append(num)

    # appends 0 if lenghs of lines aren't equal
    for num in range(0, len(line)):
        if len(second_new_line) != len(line):
            second_new_line.append(0)

    return second_new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # initialize class properties
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        self.initial_indices = {UP: [[0, col] for col in range(self.grid_width)],
                                DOWN: [[self.grid_height - 1, col] for col in range(self.grid_width)],
                                LEFT: [[row, 0] for row in range(self.grid_height)],
                                RIGHT: [[row, self.grid_width - 1] for row in range(self.grid_height)]}


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """

        # creates grid based on input width and height
        self.grid = [[0 for col in range(self.grid_width)]
                        for row in range(self.grid_height)]

        # adds two new tiles to the grid
        for num in range(0, 2):
            self.new_tile()

        return self.grid

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        string_grid = ""
        for row in range(self.grid_height):
            string_grid += str(self.grid[row]) + "\n"

        return string_grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def traverse_grid(self, start_cell, direction, num_steps):
        list = []
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]

            list.append(self.grid[row][col])

        new_list = merge(list)

        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]

            self.grid[row][col] = new_list[step]


    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        initial_list = self.initial_indices[direction]
        steps = self.grid_height
        temp_list = []

        for idx in initial_list:
                self.traverse_grid((idx), (OFFSETS[direction]), steps)

        #return ""

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        flag = True
        col = 0
        row = 0

        # gets random coordinates for a rile
        while flag:
            col = random.randrange(self.grid_width)
            row = random.randrange(self.grid_height)
            if self.grid[row][col] == 0:
                flag = False

        # gives a 2 or 4 based on specified probability
        if random.random() <= .1:
            self.grid[row][col] = 4
        else:
            self.grid[row][col] = 2


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


test_game = TwentyFortyEight(3, 3)
poc_2048_gui.run_gui(test_game)
print test_game.grid
print
print test_game.__str__()
print
test_game.move(UP)
print test_game.__str__()
