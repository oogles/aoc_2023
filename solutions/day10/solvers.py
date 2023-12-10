from aoc.utils.parsing import split_lines

input_parser = split_lines

relative_coords_map = {
    '|': ((0, -1), (0, 1)),
    '-': ((-1, 0), (1, 0)),
    'L': ((0, -1), (1, 0)),
    'J': ((0, -1), (-1, 0)),
    '7': ((0, 1), (-1, 0)),
    'F': ((0, 1), (1, 0)),
}


def traverse_maze(maze):
    
    # Find the coordinates of the starting pipe
    start = None
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == 'S':
                start = (x, y)
                break
        
        if start is not None:
            break
    
    start_x, start_y = start
    last_pipe = ('S', start_x, start_y)
    next_pipe = None
    
    # Search around the starting pipe for a valid connecting pipe
    check_coords = (
        (start_x, start_y - 1, '|F7'), (start_x, start_y + 1, '|JL'),
        (start_x - 1, start_y, '-FL'), (start_x + 1, start_y, '-J7'),
    )
    
    for x, y, valid_pipes in check_coords:
        symbol = maze[y][x]
        if symbol in valid_pipes:
            next_pipe = (symbol, x, y)
            break
    
    # Traverse the pipe maze and count the steps required to do so
    steps = 2  # start pipe and first adjacent pipe
    while next_pipe[0] != 'S':
        symbol, x, y = next_pipe
        
        relative_coords = relative_coords_map[symbol]
        
        for rel_x, rel_y in relative_coords:
            next_x = x + rel_x
            next_y = y + rel_y
            if next_x < 0 or next_y < 0:
                raise ValueError('Out of bounds')
            
            if next_x == last_pipe[1] and next_y == last_pipe[2]:
                continue
            
            last_pipe = next_pipe
            next_pipe = (maze[next_y][next_x], next_x, next_y)
            
            steps += 1
            break
    
    return steps


def part1(input_data):
    
    steps = traverse_maze(input_data)
    
    # The furthest distance from the starting point is the mid-way point of
    # the loop
    return steps // 2


def part2(input_data):
    
    raise NotImplementedError()
