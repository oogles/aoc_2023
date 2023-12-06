def input_parser(input_data):
    
    # There are only 2 rows: times and distances
    times, distances = input_data.splitlines()
    
    # Split by whitespace to get the individual values. Ignore the first
    # item, which is the label for the row
    times = times.split()[1:]
    distances = distances.split()[1:]
    
    return (times, distances)


def get_win_options(time, distance_record):
    
    # Find the minimum amount of time required to hold the button in
    # order to beat the record
    min_hold = 0
    distance = 0
    while distance <= distance_record:
        min_hold += 1
        distance = min_hold * (time - min_hold)
    
    # The time holding and the time travelling both contribute equally to
    # the distance travelled (e.g. holding for 1ms and travelling for 6ms,
    # and holding for 6ms and travelling for 1ms both result in a distance
    # travelled of 5mm). Therefore, the longest time the button can be
    # held and still beat the record is the total time less the minimum
    # holding time.
    max_hold = time - min_hold
    
    # The difference between the two gives the number of ways the record
    # can be beaten
    return max_hold - min_hold + 1


def part1(input_data):
    
    times, distances = input_data
    
    # Combine the time and distance values for individual races into a
    # single list, converting to ints at the same time
    races = zip(map(int, times), map(int, distances))
    
    win_options_product = 1
    for time, distance_record in races:
        win_options_product *= get_win_options(time, distance_record)
    
    return win_options_product


def part2(input_data):
    
    times, distances = input_data
    
    # Combine times and distances to give a single value for each
    time = int(''.join(times))
    distance = int(''.join(distances))
    
    return get_win_options(time, distance)
