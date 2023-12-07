from enum import Enum

card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'j': 1  # joker
}


class HandType(Enum):
    
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:
    
    def __init__(self, cards, bid, use_jokers=False):
        
        self.bid = bid
        
        self.cards = cards
        
        # When jokers are in play, replace Jacks with Jokers for the purposes
        # of storing card values for tie breaking
        if use_jokers:
            cards = cards.replace('J', 'j')
        
        self.card_values = [card_values[c] for c in cards]
        
        # Remove any jokers that may be present for the purposes of determining
        # the hand type
        num_jokers = cards.count('j')
        cards = cards.replace('j', '')
        
        num_unique_cards = len(set(cards))
        if num_unique_cards == 1:
            # Only one unique card means five of a kind. This is true even if
            # jokers have been removed, as they will complete the set.
            self.hand_type = HandType.FIVE_OF_A_KIND
        elif num_unique_cards == 2:
            # The first card will be either one of the two unique cards in the
            # hand. If it appears either once or four times, the hand is four
            # of a kind. Otherwise, it's a full house (the first card will
            # appear 2 or 3 times).
            # When jokers are in play, the first card can appear less than 4
            # times and still be considered four of a kind, as the jokers will
            # complete the set.
            if cards.count(cards[0]) in (1, (4 - num_jokers)):
                self.hand_type = HandType.FOUR_OF_A_KIND
            else:
                self.hand_type = HandType.FULL_HOUSE
        elif num_unique_cards == 3:
            if num_jokers:
                # When jokers are in play, the hand will always be three of a
                # kind. To have 3 unique cards, there is either one pair and
                # one joker (in which case the joker makes it three of a kind),
                # or there are no pairs and two jokers (in which case the
                # jokers also make it three of a kind).
                self.hand_type = HandType.THREE_OF_A_KIND
            else:
                # The first card can be any one of the three unique cards in the
                # hand, so it cannot be used to uniquely determine the hand type.
                # Instead, count the occurrences of the first two cards. If either
                # appears three times, or both appear once, the hand is three of
                # a kind. Otherwise, it's two pair.
                first_count = cards.count(cards[0])
                second_count = cards.count(cards[1])
                if first_count == 3 or second_count == 3 or first_count == second_count == 1:
                    self.hand_type = HandType.THREE_OF_A_KIND
                else:
                    self.hand_type = HandType.TWO_PAIR
        elif num_unique_cards == 4:
            # Whether jokers are in play or not, the hand can only ever be
            # one pair.
            self.hand_type = HandType.ONE_PAIR
        else:
            # This means either 5 unique cards or, when jokers are in play,
            # 0 unique cards (i.e. all jokers, five of a kind)
            if num_jokers:
                self.hand_type = HandType.FIVE_OF_A_KIND
            else:
                self.hand_type = HandType.HIGH_CARD
    
    def __lt__(self, other):
        
        if self.hand_type.value == other.hand_type.value:
            for i in range(len(self.card_values)):
                if self.card_values[i] == other.card_values[i]:
                    continue
                else:
                    return self.card_values[i] < other.card_values[i]
            
            return False
        else:
            return self.hand_type.value < other.hand_type.value
    
    def get_winnings(self, rank):
        
        return self.bid * rank


def input_parser(input_data):
    
    lines = []
    for line in input_data.splitlines():
        cards, bid = line.split()
        lines.append((cards, int(bid)))
    
    return lines


def part1(input_data, use_jokers=False):
    
    hands = [Hand(cards, bid, use_jokers) for cards, bid in input_data]
    total_winnings = 0
    
    for i, hand in enumerate(sorted(hands), start=1):
        total_winnings += hand.get_winnings(i)
    
    return total_winnings


def part2(input_data):
    
    return part1(input_data, use_jokers=True)
