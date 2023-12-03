class Number:
    
    def __init__(self):
        
        self.value = ''
        self.coords = []
    
    def add_character(self, character, x, y):
        
        self.value += character
        self.coords.append((x, y))
    
    def is_adjacent_to(self, symbol):
        
        # If any of the number's coordinates are within a distance of 1
        # from the given symbol's coordinates, it is adjacent
        symbol_x = symbol.x
        symbol_y = symbol.y
        
        for x, y in self.coords:
            if abs(x - symbol_x) <= 1 and abs(y - symbol_y) <= 1:
                return True
        
        return False


class Symbol:
    
    def __init__(self, character, x, y):
        
        self.value = character
        self.x = x
        self.y = y


def input_parser(input_data):
    
    schematic = []
    
    # Find all numbers and symbols, along with the coordinates of the engine
    # schematic they occupy
    for y, line in enumerate(input_data.splitlines()):
        schematic_row = []
        
        current_number = Number()
        for x, character in enumerate(line):
            if character.isdigit():
                current_number.add_character(character, x, y)
            else:
                if current_number.value:
                    # Store the now-complete number and reset `current_number`
                    schematic_row.append(current_number)
                    current_number = Number()
                
                if character != '.':
                    schematic_row.append(Symbol(character, x, y))
        
        # If the row ended on a numeric character, store the last number
        if current_number.value:
            schematic_row.append(current_number)
        
        schematic.append(schematic_row)
    
    return schematic


def part1(schematic):
    
    schematic_length = len(schematic)
    parts_total = 0
    
    # Analyse matrix to find all numbers adjacent to symbols
    for y, row in enumerate(schematic):
        min_y = max(0, y - 1)
        max_y = min(schematic_length, y + 1)
        adjacent_rows = schematic[min_y:max_y + 1]
        
        for item in row:
            if isinstance(item, Symbol):
                for adj_row in adjacent_rows:
                    for other_item in adj_row:
                        if isinstance(other_item, Number) and other_item.is_adjacent_to(item):
                            parts_total += int(other_item.value)
    
    return parts_total


def part2(schematic):
    
    schematic_length = len(schematic)
    gear_ratio_sum = 0
    
    # Analyse matrix to find all gears (`*` symbols adjacent to two part numbers)
    for y, row in enumerate(schematic):
        min_y = max(0, y - 1)
        max_y = min(schematic_length, y + 1)
        adjacent_rows = schematic[min_y:max_y + 1]
        
        for item in row:
            if item.value == '*':
                adjacent_parts = []
                
                for adj_row in adjacent_rows:
                    for other_item in adj_row:
                        if isinstance(other_item, Number) and other_item.is_adjacent_to(item):
                            adjacent_parts.append(other_item)
                
                if len(adjacent_parts) == 2:
                    # Calculate the gear ratio and add it to the total
                    part1, part2 = adjacent_parts
                    gear_ratio = int(part1.value) * int(part2.value)
                    gear_ratio_sum += gear_ratio
    
    return gear_ratio_sum
