from utils import get_input_lines


def solve_1():
    predictions = []
    for line in get_input_lines():
        numbers = tuple(map(int, line.split()))
        predictions.append(get_next(numbers))
    return sum(predictions)


def solve_2():
    predictions = []
    for line in get_input_lines():
        numbers = tuple(reversed(list(map(int, line.split()))))
        predictions.append(get_next(numbers))
    return sum(predictions)


def get_next(numbers):
    differences = get_differences(numbers)
    difference = differences[0] if len(set(differences)) == 1 else get_next(differences)
    return numbers[-1] + difference


def get_differences(numbers):
    return [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]