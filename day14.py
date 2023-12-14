from utils import get_input_lines


def apply(layout):
    for i, line in enumerate(layout):
        if i == 0: continue
        for j in range(i):
            k = i - j
            for l in range(len((line))):
                if layout[k][l] == 'O' and layout[k-1][l] == '.':
                    layout[k-1] = layout[k-1][:l] + 'O' + layout[k-1][l+1:]
                    layout[k] = layout[k][:l] + '.' + layout[k][l+1:]
    return layout


def rotate(grid):
    height, width = len(grid), len(grid[0])
    new_grid = [[None for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for j in range(width):
            new_grid[j][height-i-1] = grid[i][j]
    return [''.join(row) for row in new_grid]


def get_weight(layout):
    return sum(
        row.count('O') * (len(layout) - i)
        for i, row in enumerate(layout)
    )


def solve_2(n):

    layout = list(get_input_lines())

    m = {}
    weights = []
    start, end = None, None

    # Move the boulders
    for i in range(n):

        for j in range(4):
            layout = apply(layout)
            layout = rotate(layout)
        weight = get_weight(layout)
        weights.append(weight)
        
        key = tuple(tuple(row) for row in layout)
        if key in m:
            start, end = m[key], i
            break
        else:
            m[key] = i
            
    # Fast forward
    weights = weights[start:end]
    steps = n - start -1
    return weights[steps % len(weights)]

        






def solve_1():

    layout = list(get_input_lines())

    # Move up the boulders
    for i, line in enumerate(layout):
        if i == 0: continue
        for j in range(i):
            k = i - j
            for l in range(len((line))):
                if layout[k][l] == 'O' and layout[k-1][l] == '.':
                    layout[k-1] = layout[k-1][:l] + 'O' + layout[k-1][l+1:]
                    layout[k] = layout[k][:l] + '.' + layout[k][l+1:]

    # Calculate the weight
    weight = sum(
        row.count('O') * (len(layout) - i)
        for i, row in enumerate(layout)
    )

    return weight
