from utils import get_input_lines


def solve_1():
    count = 0
    for line in get_input_lines():
        pattern, counts = line.split()
        counts = tuple(map(int, counts.split(',')))
        count += resolve(pattern, counts)
    return count


def resolve(pattern, counts):
    return sum(validate(p, counts) for p in options(pattern))


def validate(pattern, counts):
    groups = split(pattern)
    groups = [g for g in groups if '#' in g]
    if len(groups) == len(counts):
        for g, c in zip(groups, counts):
            if len(g) != c:
                return False
        return True
    return False


def options(pattern):
    c = pattern[0]
    opts = '#.' if c == '?' else c
    for o in opts:
        if not pattern[1:]:
            yield o
        else:
            for oo in options(pattern[1:]):
                yield o + oo


def split(pattern):
    groups = []
    buf = ''
    for c in pattern:
        if not buf or c == buf[-1]:
            buf += c
        else:
            groups.append(buf)
            buf = c
    groups.append(buf)
    return groups
