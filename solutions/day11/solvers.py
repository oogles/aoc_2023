from itertools import combinations

from aoc.utils import parsing

input_parser = parsing.split_lines


def part1(input_data, expansion_rate=1):
    
    expansion_rate = max(1, expansion_rate - 1)
    
    # Get the x, y coordinates of each galaxy (#) in the map. Also track which
    # rows and columns contain galaxies, in order to find those that don't
    # contain any.
    galaxies = []
    non_empty_rows = set()
    non_empty_cols = set()
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.append((x, y))
                non_empty_rows.add(y)
                non_empty_cols.add(x)
    
    # Get a list of all the rows and columns that don't contain any galaxies
    empty_rows = set(range(len(input_data))) - non_empty_rows
    empty_cols = set(range(len(input_data[0]))) - non_empty_cols
    
    # Iterate over the list of galaxies and increment the coordinates of any
    # that occur in a row/column AFTER an empty one - accounting for the
    # "expansion" of empty regions of space
    for i, (x, y) in enumerate(galaxies):
        new_x = x
        for empty_x in sorted(empty_cols):
            if x > empty_x:
                new_x += expansion_rate
            else:
                break
        
        new_y = y
        for empty_row in sorted(empty_rows):
            if y > empty_row:
                new_y += expansion_rate
            else:
                break
        
        galaxies[i] = (new_x, new_y)
    
    # Get all distinct pairs of galaxies, and the manhattan distance between them
    galaxy_pairs = combinations(galaxies, 2)
    distance_sum = 0
    for (x1, y1), (x2, y2) in galaxy_pairs:
        distance_sum += abs(x1 - x2) + abs(y1 - y2)
    
    return distance_sum


def part2(input_data):
    
    return part1(input_data, expansion_rate=1000000)
