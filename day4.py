from utils import get_input_lines


def solve_1():
    total = 0
    for line in get_input_lines():
        winning, possesed = line.split(': ')[1].split(' | ')
        winning, possesed = set(winning.split()), set(possesed.split())
        matches = len(winning & possesed)
        score = 2 ** (matches - 1) if matches else 0
        total += score
    return total


def solve_2():
    
    # To parse each card
    def evaluate(line):
        card, numbers = line.split(': ')
        card = int(card.split()[-1])
        winning, possesed = numbers.split(' | ')
        winning, possesed = set(winning.split()), set(possesed.split())
        matches = len(winning & possesed)
        score = 2 ** (matches - 1) if matches else 0
        return card, matches
    
    # Mapping between card number and number of matches
    cards = dict(map(evaluate, get_input_lines()))

    # To recursively evaluate the number of cards won with the card with the given number, with
    # memoization to avoid already processed cards
    cache = {}
    def calculate(n):
        if n in cache: return cache[n] # memoize
        matches = cards[n]
        return matches + sum(calculate(m) for m in range(n+1, n+1+matches))
    
    # To get the total number of cards won, on top of the ones already possesed
    result = sum(calculate(card) for card in sorted(cards)) + len(cards)    
    return result

