def input_parser(input_data):
    
    games = []
    
    for line in input_data.splitlines():
        game_id_part, showings_part = line.split(': ')
        
        game_id = game_id_part.replace('Game ', '')
        
        max_counts = {}
        for showing in showings_part.split('; '):
            for hint in showing.split(', '):
                count, colour = hint.split(' ')
                count = int(count)
                
                if colour not in max_counts or count > max_counts[colour]:
                    max_counts[colour] = count
        
        games.append({
            'id': int(game_id),
            'max_counts': max_counts
        })
    
    return games


def part1(input_data):
    
    max_red = 12
    max_green = 13
    max_blue = 14
    
    possible_games = []
    
    for game in input_data:
        if game['max_counts'].get('red', 0) > max_red:
            continue
        
        if game['max_counts'].get('green', 0) > max_green:
            continue
        
        if game['max_counts'].get('blue', 0) > max_blue:
            continue
        
        possible_games.append(game['id'])
    
    return sum(possible_games)


def part2(input_data):
    
    power_sum = 0
    
    for game in input_data:
        red = game['max_counts'].get('red', 0)
        green = game['max_counts'].get('green', 0)
        blue = game['max_counts'].get('blue', 0)
        
        power = red * green * blue
        power_sum += power
    
    return power_sum
