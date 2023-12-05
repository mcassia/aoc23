from utils import get_input_lines


def parse_line(line):
    game, sets = line.split(': ')
    game = int(game.split()[-1])
    sets = sets.split(';')
    sets = [
        {
            x.split()[1]: int(x.split()[0])
            for x in s.strip().split(', ')
        }
        for s in sets
    ]
    return game, sets




def solve_1():
    
    maximum = {'red': 12, 'green': 13, 'blue': 14}
    valid = []

    for line in get_input_lines():
        game, sets = parse_line(line)
        possible = all(
            all(count <= maximum[color] for color, count in s.items())
            for s in sets
        )
        if possible:
            valid.append(game)

    return sum(valid)


def solve_2():

    total = 0

    for line in get_input_lines():
        game, sets = parse_line(line)
        minimum = {'red': 0, 'green': 0, 'blue': 0}
        for s in sets:
            for color, count in s.items():
                minimum[color] = max(minimum[color], count)
        power = minimum.get('red', 1) * minimum.get('green', 1) * minimum.get('blue', 1)
        total += power

    return total
        