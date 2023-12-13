from utils import get_input_lines


def solve(smudges):
    total = 0
    for area in parse():
        # For each area, find the axis of symmetry, either vertically or horizontally, allowing
        # a certain number of smudges (i.e. flipped bits)
        i, multiplier = find_simmetry(area, smudges=smudges), 100
        if i is None:
            i, multiplier = find_simmetry(rotate(area), smudges=smudges), 1
        total += i * multiplier
    return total


def solve_1():
    return solve(smudges=0)


def solve_2():
    return solve(smudges=1)


def parse():
    area = []
    for line in get_input_lines():
        if not line:
            yield area
            area = []
        else:
            area.append(line)
    if area:
        yield area
        

def get_difference_count(a, b):
    return sum(x != y for x, y in zip(a, b))
        

def find_simmetry(area, smudges=0):
    # For each possible axis of symmetry, fetch all the rows above and below the axis (ensuring the
    # same number for both is used), and check for differences against the required smudges.
    for i in range(1, len(area)):
        before, after = area[:i], area[i:]
        before = list(reversed(before))
        differences = 0
        for a, b in zip(before, after):
            differences += get_difference_count(a, b)
        if differences == smudges:
            return i
        

def rotate(grid):
    height, width = len(grid), len(grid[0])
    new_grid = [[None for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for j in range(width):
            new_grid[j][height-i-1] = grid[i][j]
    return [''.join(row) for row in new_grid]
        


