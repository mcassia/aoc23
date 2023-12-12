from utils import get_input_lines


def solve_1():
    return solve(1)


def solve_2():
    return solve(5)


def solve(multiplier=1):

    total = 0

    lines = get_input_lines()
    for i, line in enumerate(lines):

        pattern, counts = line.split()
        pattern = '?'.join(pattern for _ in range(multiplier))
        counts = ','.join(counts for _ in range(multiplier))

        counts = tuple(map(int, counts.split(',')))

        result = resolve(pattern, counts)
        total += result

    return total


CACHE = {}

def resolve(pattern, counts):

    # If this specific pattern and counts combination was already encountered, then fetch the
    # result from cache, as it's guaranteed to be the same, regardless of origin
    key = (pattern, counts)
    if key in CACHE:
        return CACHE[key]

    # If no more segments are to be placed, determine if it's a valid termination
    if not counts:
        return '#' not in pattern

    # All the possible indices from where to start filling
    indices = []
    for i, c in enumerate(pattern):
        if c == '?':
            indices.append(i)
        elif c == '#':
            indices.append(i)
            break

    # Search
    total = 0
    n = counts[0]
    for i in indices:
        sub = pattern[i:i+n]
        if len(sub) != n: continue
        if '.' in sub: continue
        if pattern[i+n:i+n+1] == '#': continue
        total += int(resolve(pattern[i+n+1:], counts[1:]))

    CACHE[key] = total

    return total