def input_parser(input_data):
    
    return input_data.strip().split(',')


def hash(value):
    
    result = 0
    for char in value:
        result += ord(char)
        result *= 17
        result %= 256
    
    return result


def part1(input_data):
    
    return sum(hash(step) for step in input_data)


def part2(input_data):
    
    boxes = {}
    focal_lengths = {}
    
    for step in input_data:
        if '=' in step:
            label, focal_length = step.split('=')
        else:
            label = step.split('-')[0]
            focal_length = None
        
        box_number = hash(label)
        boxes.setdefault(box_number, [])
        box = boxes[box_number]
        
        if not focal_length:
            # No focal length means a '-' instruction: remove the lens
            # with the specified label
            try:
                box.remove(label)
            except ValueError:
                pass
        else:
            # Add a lens of the specified focal length to the box
            focal_lengths[label] = int(focal_length)
            
            # If a lens already exists, it is replaced (meaning no change
            # to the labels of lenses in the box). Otherwise, it is added
            # behind any existing lenses.
            if label not in box:
                box.append(label)
    
    focusing_power = 0
    for box_number, lenses in boxes.items():
        box_number += 1
        for i, label in enumerate(lenses, start=1):
            focal_length = focal_lengths[label]
            focusing_power += box_number * i * focal_length
    
    return focusing_power
