from utils import get_input_lines


def solve_1():
    numbers = []
    for line in get_input_lines():
        digits = [c for c in line if c.isdigit()]
        number = int(digits[0] + digits[-1])
        numbers.append(number)
    return sum(numbers)


def solve_2():

    total = 0
    words = 'zero one two three four five six seven eight nine'.split()

    for line in get_input_lines():

        # Replace each digit as a word into a string, allowing overlaps (e.g. "eightwo" should map
        # to "82").
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
                continue
            for j, word in enumerate(words):
                if line[i:].startswith(word):
                    digits.append(str(j))
                    break
        total += int(digits[0] + digits[-1])

    return total
