def input_parser(input_data):
    
    lines = []
    for line in input_data.splitlines():
        lines.append(tuple(map(int, line.split())))
    
    return lines


def part1(input_data, invert=False):
    
    diff_multiplier = 1 if invert else -1
    prediction_value_index = 0 if invert else -1
    
    prediction_sum = 0
    
    for line in input_data:
        # Only keep the last full sequence of values, starting with the initial
        # history sequence
        last_sequence = line
        
        # But keep the final number in every sequence, starting with the last
        # entry in the history sequence
        prediction_values = [line[prediction_value_index]]
        
        while True:
            diff_sequence = []
            for i in range(len(last_sequence) - 1):
                diff_sequence.append((last_sequence[i] - last_sequence[i + 1]) * diff_multiplier)
            
            # If the diff sequence is all zeros, stop here
            if all(i == 0 for i in diff_sequence):
                break
            
            last_sequence = diff_sequence
            prediction_values.append(diff_sequence[prediction_value_index])
        
        prediction_sum += sum(prediction_values)
    
    return prediction_sum


def part2(input_data):
    
    return part1(input_data, invert=True)
