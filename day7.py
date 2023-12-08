from utils import get_input_lines
from collections import Counter


CARDS_1 = 'A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'.split(', ')
CARD_1_TO_VALUE = {card: i for i, card in enumerate(CARDS_1)}
CARDS_2 = 'A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J'.split(', ')
CARD_2_TO_VALUE = {card: i for i, card in enumerate(CARDS_2)}


def evaluate_hand(hand, joker=False):

    # If 'J' is treated as joker
    if joker:
        if 'J' in hand:
            i = hand.index('J')
            return min(
                evaluate_hand(hand[:i] + card + hand[i+1:], joker=True)
                for card in CARDS_2
                if card != 'J'
            )

    # Find the correct hand type based on counts
    counts = sorted(dict(Counter(hand)).values())
    types = [[5], [1, 4], [2, 3], [1, 1, 3], [1, 2, 2], [1, 1, 1, 2]]
    for i, t in enumerate(types):
        if t == counts:
            return i
    return len(types)


def solve_1():
    
    # Parse and evaluate hands
    hands = [(line.split()[0], int(line.split()[1])) for line in get_input_lines()]
    hands = [(hand, bid, evaluate_hand(hand)) for hand, bid in hands]
    
    # Sort by value and resolve ties
    hands = sorted(
        hands,
        key=lambda hand: (hand[2], *(CARD_1_TO_VALUE[c] for c in hand[0]))
    )
    hands = list(reversed(hands))

    # Calculate winnings
    winnings = sum(
        rank * bid
        for rank, (_, bid, _) in enumerate(hands, 1)
    )

    return winnings


def solve_2():
    
    # Parse and evaluate hands
    hands = [(line.split()[0], int(line.split()[1])) for line in get_input_lines()]
    hands = [(hand, bid, evaluate_hand(hand, joker=True)) for hand, bid in hands]
    
    # Sort by value and resolve ties
    hands = sorted(
        hands,
        key=lambda hand: (hand[2], *(CARD_2_TO_VALUE[c] for c in hand[0]))
    )
    hands = list(reversed(hands))

    # Calculate winnings
    winnings = sum(
        rank * bid
        for rank, (_, bid, _) in enumerate(hands, 1)
    )

    return winnings