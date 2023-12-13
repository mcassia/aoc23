from utils import get_input_lines


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


def find_simmetry(area):
    for i in range(1, len(area)):
        before, after = area[:i], area[i:]
        before = list(reversed(before))
        for a, b in zip(before, after):
            if a != b: break
        else:
            return i
        

def get_difference_count(a, b):
    return sum(
        x != y for x, y in zip(a, b)
    )
        

def find_simmetry_2(area):
    for i in range(1, len(area)):
        before, after = area[:i], area[i:]
        before = list(reversed(before))
        differences = 0
        for a, b in zip(before, after):
            differences += get_difference_count(a, b)
        if differences == 1:
            return i
        

def rotate(grid):
    height, width = len(grid), len(grid[0])
    new_grid = [[None for _ in range(height)] for _ in range(width)]
    for i in range(height):
        for j in range(width):
            new_grid[j][height-i-1] = grid[i][j]
    return [''.join(row) for row in new_grid]
        


def solve_1():

    total = 0

    for area in parse():

        i, multiplier = find_simmetry(area), 100
        if i is None:
            i, multiplier = find_simmetry(rotate(area)), 1

        total += i * multiplier

    return total


def solve_2():

    total = 0

    for area in parse():

        i, multiplier = find_simmetry_2(area), 100
        if i is None:
            i, multiplier = find_simmetry_2(rotate(area)), 1

        total += i * multiplier

    return total



            
            
            