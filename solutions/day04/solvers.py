def input_parser(input_data):
    
    cards = []
    
    for line in input_data.splitlines():
        _, numbers = line.split(': ')
        winning_numbers, present_numbers = numbers.split(' | ')
        
        winning_numbers = set(map(int, winning_numbers.split()))
        present_numbers = set(map(int, present_numbers.split()))
        
        cards.append((winning_numbers, present_numbers))
    
    return cards


def part1(cards):
    
    points_sum = 0
    
    for winning_numbers, present_numbers in cards:
        matches = len(winning_numbers & present_numbers)
        if matches:
            points_sum += 2 ** (matches - 1)
    
    return points_sum


def part2(cards):
    
    # Keep a count of the number of cards won by each card
    counts = {}
    
    def process_card(index):
        
        # If this card has already been fully processed, return the known count
        if index in counts:
            return counts[index]
        
        winning_numbers, present_numbers = cards[index]
        matches = len(winning_numbers & present_numbers)
        
        count = 1  # start with the original card
        
        for i in range(matches):
            count += process_card(index + i + 1)
        
        counts[index] = count
        
        return count
    
    for i in range(len(cards)):
        process_card(i)
    
    return sum(counts.values())


def part2_old(cards):
    
    # Keep a count of all cards, either original or won. Start with a count of
    # 1 for each original card.
    counts = {i: 1 for i in range(len(cards))}
    
    def process_card(index):
        
        winning_numbers, present_numbers = cards[index]
        matches = len(winning_numbers & present_numbers)
        
        for i in range(matches):
            j = index + i + 1
            counts[j] += 1
            process_card(j)
    
    for i in range(len(cards)):
        process_card(i)
    
    return sum(counts.values())
