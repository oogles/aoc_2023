from aoc.utils import parsing

input_parser = parsing.split_lines

digit_word_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def find_digit(line, reverse=False):
    
    start = 0
    stop = len(line) + 1
    step = 1
    
    # If searching in reverse, start from the end of the line and go backwards
    if reverse:
        start = -1
        stop *= -1
        step *= -1
    
    # Search character-by-character to avoid situations like "eightwo"
    # being detected as "two", when it should be "eight"
    for i in range(start, stop, step):
        if line[i].isdigit():
            return line[i]
        
        if reverse:
            substr = line[i:]
        else:
            substr = line[:i + step]
        
        for word, digit in digit_word_map.items():
            if word in substr:
                return digit


def part1(input_data):
    
    # Strip all non-numeric characters from each line
    lines = [tuple(filter(str.isdigit, line)) for line in input_data]
    
    # Combine first and last digits on each line
    numbers = [f'{i[0]}{i[-1]}' for i in lines]
    
    # Sum the resulting integers
    return sum(map(int, numbers))


def part2(input_data):
    
    numbers = []
    
    # Find the first and last occurrence, on each line, of a single-digit
    # number - either as a digit or spelled out as a word
    for line in input_data:
        first_digit = find_digit(line)
        last_digit = find_digit(line, reverse=True)
        
        numbers.append(f'{first_digit}{last_digit}')
    
    return part1(numbers)
