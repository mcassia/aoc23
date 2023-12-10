from utils import get_input_lines
from collections import defaultdict


PIPES = {
    '-': ((0, -1), (0, +1)),
    '|': ((-1, 0), (+1, 0)),
    'L': ((-1, 0), (0, +1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((+1, 0), (0, -1)),
    'F': ((+1, 0), (0, +1)),
}
REVERSED_PIPES = {v: k for k, v in PIPES.items()}


def solve_1():

    # Parse the input to generate a graph
    start, lines = None, get_input_lines()
    layout = {(i, j): c for i, row in enumerate(lines) for j, c in enumerate(row)}
    for (i, j), c in layout.items():
        if c == 'S':
            start = (i, j)
    assert start

    # Resolve the correct tile for the starting position
    layout[start] = resolve(*start, layout)

    # Traverse from the start following the pipes' orientations to determine the main loop
    nodes, visited, depth = {start}, {}, 0
    while nodes:
        next_nodes = set()
        for i, j in nodes:
            visited[(i, j)] = depth
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i + di, j + dj
                pipe = PIPES.get(layout.get((ni, nj)))
                if not pipe: continue
                if not (-di, -dj) in pipe: continue
                this_pipe = PIPES.get(layout.get((i, j)))
                if not (di, dj) in this_pipe: continue
                next_nodes.add((ni, nj))
        depth += 1
        nodes = next_nodes - set(visited)

    return max(visited.values())


def solve_2():

    # Parse the input to generate a graph
    start, lines = None, get_input_lines()
    height, width = len(lines), len(lines[0])
    layout = {(i, j): c for i, row in enumerate(lines) for j, c in enumerate(row)}
    for (i, j), c in layout.items():
        if c == 'S':
            start = (i, j)
    assert start

    # Resolve the correct tile for the starting position
    layout[start] = resolve(*start, layout)

    # Traverse from the start following the pipes' orientations to determine the main loop
    nodes, visited, depth = {start}, {}, 0
    while nodes:
        next_nodes = set()
        for i, j in nodes:
            visited[(i, j)] = depth
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i + di, j + dj
                pipe = PIPES.get(layout.get((ni, nj)))
                if not pipe: continue
                if not (-di, -dj) in pipe: continue
                this_pipe = PIPES.get(layout.get((i, j)))
                if not (di, dj) in this_pipe: continue
                next_nodes.add((ni, nj))
        depth += 1
        nodes = next_nodes - set(visited)

    # Any node that has not been visited should be replaced with '.' (i.e. "junk pipes")
    for (i, j), c in layout.items():
        if (i, j) not in visited:
            layout[(i, j)] = '.'

    # Expand the layout to add gaps, since squeezing through pipes is a thing ¯\_(ツ)_/¯
    layout = {(i*2, j*2): c for (i, j), c in layout.items()}
    for i in range(height*2):
        for j in range(width*2):
            if (i, j) not in layout:
                c = resolve(i, j, layout)
                layout[(i, j)] = c or ' '
    
    # Track every group of '.' or ' ' (i.e. cliques/islands), by traversing each location, finding
    # a matching one and previously unexplored, finding all of its similar neighbours
    groups = []
    for (i, j), c in layout.items():
        if c not in ('.', ' '): continue
        if any((i, j) in group for group in groups): continue
        visited, nodes = set(), {(i, j)}
        while nodes:
            next_nodes = set()
            for ai, aj in nodes:
                visited.add((ai, aj))
                for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ni, nj = ai + di, aj + dj
                    if layout.get((ni, nj)) in ('.', ' '):
                        next_nodes.add((ni, nj))
            nodes = next_nodes - visited
        groups.append(visited)

    # Disregard any group which has any location touching any of the edges
    groups = [
        group for group in groups
        if all(
            i not in (0, height*2-1) and j not in (0, width*2-1)
            for i, j in group
        )
    ]

    # Find the number of '.' (and not ' ') in the retained groups
    return sum(
        layout[c] == '.'
        for group in groups
        for c in group
    )


def resolve(i, j, layout):
    """
    Finds the tile at the given location in the layout that fits two other neighbouring tiles,
    if any.    
    """
    for ai, aj in [(0,1),(0,-1),(1,0),(-1,0)]:
        for bi, bj in [(0,1),(0,-1),(1,0),(-1,0)]:
            if (ai, aj) == (bi, bj): continue
            a, b = (i + ai, j + aj), (i + bi, j + bj)
            pa, pb = PIPES.get(layout.get(a)), PIPES.get(layout.get(b))
            if not pa or not pb: continue
            if (-ai, -aj) in pa and (-bi, -bj) in pb:
                p = REVERSED_PIPES.get(((ai, aj), (bi, bj))) or REVERSED_PIPES.get(((bi, bj), (ai, aj)))
                return p