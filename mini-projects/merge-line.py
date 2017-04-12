# crude method for taking a line in the faux 2048 game and shifting the numbers left appropriately

"""
Merge function for 2048 game.
"""

# sample line for testing
a_line = [2, 0, 2, 2]

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
    for i in range(0, len(line)):
        if len(first_new_line) != len(line):
            first_new_line.append(0)

    # adds same numbers together
    for i in range(0, (len(line) - 1)):
        if first_new_line[i] == first_new_line[i + 1]:
            first_new_line[i] += first_new_line[i + 1]
            first_new_line[i + 1] = 0

    # appends num if num isn't 0
    for num in first_new_line:
        if num != 0:
            second_new_line.append(num)

    # appends 0 if lenghs of lines aren't equal
    for i in range(0, len(line)):
        if len(second_new_line) != len(line):
            second_new_line.append(0)

    return second_new_line

print merge(a_line)
