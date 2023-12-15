from utils import get_input_text


def apply(text):
    value = 0
    for c in text:
        value += ord(c)
        value *= 17
        value %= 256
    return value


def solve_1():

    steps = get_input_text().strip().split(',')

    return sum(map(apply, steps))


def solve_2():

    steps = get_input_text().strip().split(',')
    boxes = [[] for _ in range(256)] # list[tuple[label: str, lens_focal_strength: int],]

    for step in steps:

        if '=' in step:
            label, lens = step.split('=')
            lens = int(lens)
            i = apply(label)
            for j, (a, b) in enumerate(boxes[i]):
                if a == label:
                    boxes[i][j] = (label, lens)
                    break
            else:
                boxes[i].append((label, lens))

        elif '-' in step:
            label = step[:-1]
            i = apply(label)
            boxes[i] = [(a, b) for a, b in boxes[i] if a != label]

    return sum(
        (i + 1) * (j + 1) * lens
        for i, box in enumerate(boxes)
        for j, (_, lens) in enumerate(box)
    )
        

