from utils import get_input_lines


def parse():

    lines = get_input_lines()

    times = map(int, lines[0].split(':')[1].strip().split())
    distances = map(int, lines[1].split(':')[1].strip().split())

    return list(zip(times, distances))


def run(time):
    for time_spent_pressing in range(0, time):
        time_left = time - time_spent_pressing
        distance = time_left * time_spent_pressing
        yield distance


def solve_1():
    
    result = 1

    for time, distance in parse():
        distances = list(run(time))
        result *= sum([d > distance for d in distances])

    return result


def solve_2():
    
    lines = get_input_lines()
    time = int(lines[0].replace(' ', '').split(':')[1].strip())
    distance = int(lines[1].replace(' ', '').split(':')[1].strip())

    distances = list(run(time))

    result = sum([d > distance for d in distances])

    return result