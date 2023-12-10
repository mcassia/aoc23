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


def solve_2():

    # Parse the input to generate a graph
    start, lines = None, get_input_lines()
    height, width = len(lines), len(lines[0])
    layout = {(i, j): c for i, row in enumerate(lines) for j, c in enumerate(row)}
    for (i, j), c in layout.items():
        if c == 'S':
            start = (i, j)
    assert start

    # Print
    def view():
        for i in range(height):
            row = ''
            for j in range(width):
                row += layout[(i, j)]
            print(row)
        print(' ')

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

    # Any node that has not been visited should be replaced with '.'
    for (i, j), c in layout.items():
        if (i, j) not in visited:
            layout[(i, j)] = '.'

    # Expand the layout to add gaps
    layout = {(i*2, j*2): c for (i, j), c in layout.items()}
    for i in range(height*2):
        for j in range(width*2):
            if (i, j) not in layout:
                c = resolve(i, j, layout)
                layout[(i, j)] = c or ' '
    
    # For every '.' which was not already found as part of a '.' group
    groups = []
    for (i, j), c in layout.items():
        if c not in ('.', ' '): continue
        if any((i, j) in group for group in groups): continue

        # Find all '.' neighbours to form a group
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

    # Disregard any group which is on the outside
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

        


# def solve_2():

#     # Parse the input to generate a graph
#     start, lines = None, get_input_lines()
#     height, width = len(lines), len(lines[0])
#     layout = {(i, j): c for i, row in enumerate(lines) for j, c in enumerate(row)}
#     for (i, j), c in layout.items():
#         if c == 'S':
#             start = (i, j)
#     assert start

#     # Resolve the correct tile for the starting position
#     layout[start] = resolve(*start, layout)

#     # Expand the layout to add gaps
#     layout = {(i*2, j*2): c for (i, j), c in layout.items()}
#     for i in range(height*2):
#         for j in range(width*2):
#             if (i, j) not in layout:
#                 c = resolve(i, j, layout)
#                 layout[(i, j)] = c or ' '

#     # Print
#     for i in range(height*2):
#         row = ''
#         for j in range(width*2):
#             row += layout[(i, j)]
#         print(row)
    
#     # For every '.' which was not already found as part of a '.' group
#     groups = []
#     for (i, j), c in layout.items():
#         if c not in ('.', ' '): continue
#         if any((i, j) in group for group in groups): continue

#         # Find all '.' neighbours to form a group
#         visited, nodes = set(), {(i, j)}
#         while nodes:
#             next_nodes = set()
#             for ai, aj in nodes:
#                 visited.add((ai, aj))
#                 for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
#                     ni, nj = ai + di, aj + dj
#                     if layout.get((ni, nj)) in ('.', ' '):
#                         next_nodes.add((ni, nj))
#             nodes = next_nodes - visited
#         groups.append(visited)

#     # Disregard any group which is on the outside
#     groups = [
#         group for group in groups
#         if all(
#             i not in (0, height*2-1) and j not in (0, width*2-1)
#             for i, j in group
#         )
#     ]

#     # Find the number of '.' (and not ' ') in the retained groups
#     return sum(
#         layout[c] == '.'
#         for group in groups
#         for c in group
#     )


def resolve(i, j, layout):
    for ai, aj in [(0,1),(0,-1),(1,0),(-1,0)]:
        for bi, bj in [(0,1),(0,-1),(1,0),(-1,0)]:
            if (ai, aj) == (bi, bj): continue
            a, b = (i + ai, j + aj), (i + bi, j + bj)
            pa, pb = PIPES.get(layout.get(a)), PIPES.get(layout.get(b))
            if not pa or not pb: continue
            if (-ai, -aj) in pa and (-bi, -bj) in pb:
                p = REVERSED_PIPES.get(((ai, aj), (bi, bj))) or REVERSED_PIPES.get(((bi, bj), (ai, aj)))
                return p
    
    

    



# def solve_2():

#     lines = get_input_lines()
#     height, width = len(lines), len(lines[0])
#     layout = {(i, j): c for i, row in enumerate(lines) for j, c in enumerate(row)}
#     groups = []

#     # For every '.' which was not already found as part of a '.' group
#     for (i, j), c in layout.items():
#         if c != '.': continue
#         if any((i, j) in group for group in groups): continue

#         # Find all '.' neighbours to form a group
#         visited, nodes = set(), {(i, j)}
#         while nodes:
#             next_nodes = set()
#             for ai, aj in nodes:
#                 visited.add((ai, aj))
#                 for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
#                     ni, nj = ai + di, aj + dj
#                     if layout.get((ni, nj)) == '.':
#                         next_nodes.add((ni, nj))
#             nodes = next_nodes - visited
#         groups.append(visited)

#     # Disregard any group which is on the outside
#     groups = [
#         group for group in groups
#         if all(
#             i not in (0, height-1) and j not in (0, width-1)
#             for i, j in group
#         )
#     ]

#     return sum(len(group) for group in groups)







def solve_1():

    # Parse the input to generate a graph
    start, lines = None, get_input_lines()
    layout = {(i, j): c for i, row in enumerate(lines) for j, c in enumerate(row)}
    for (i, j), c in layout.items():
        if c == 'S':
            start = (i, j)
    assert start

    # Determine which pipe the starting point is by finding the two neighbours pointing to it
    i, j = start
    nodes = set()
    for ai, aj in [(0,1),(0,-1),(1,0),(-1,0)]:
        for bi, bj in [(0,1),(0,-1),(1,0),(-1,0)]:
            if (ai, aj) == (bi, bj): continue
            a, b = (i + ai, j + aj), (i + bi, j + bj)
            pa, pb = PIPES.get(layout.get(a)), PIPES.get(layout.get(b))
            if not pa or not pb: continue
            if (-ai, -aj) in pa and (-bi, -bj) in pb:
                nodes = {a, b}
    assert nodes

    # Traverse from the start following the pipes' orientations
    visited, depth = {start: 0}, 1
    while nodes:
        next_nodes = set()
        for i, j in nodes:
            visited[(i, j)] = depth
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i + di, j + dj
                pipe = PIPES.get(layout.get((ni, nj)))
                if not pipe: continue
                if not (-di, -dj) in pipe: continue
                next_nodes.add((ni, nj))
        depth += 1
        nodes = next_nodes - set(visited)

    return max(visited.values())








            





# def solve_1():

#     # Parse the input to generate an adjacency graph and convert the starting point into a valid
#     # pipe
#     lines = get_input_lines()
#     height, width = len(lines), len(lines[0])
#     layout = {
#         (i, j): c
#         for i, row in enumerate(lines)
#         for j, c in enumerate(row)
#     }
#     start, graph = None, defaultdict(set)
#     for (i, j), c in layout.items():
#         if c in PIPES:
#             (ai, aj), (bi, bj) = PIPES[c]
#             a = (i+ai, j+aj)
#             b = (i+bi, j+bj)
#             if layout.get(a) in PIPES and layout.get(b) in PIPES:
#                 graph[a].add((i, j))
#                 graph[b].add((i, j))
#                 graph[(i, j)].add(a)
#                 graph[(i, j)].add(b)

#         elif c == 'S':
#             start = (i, j)
#             for (ai, aj), (bi, bj) in PIPES.values():
#                 a = (i + ai), (j + aj)
#                 b = (i + bi), (j + bj)
#                 if not layout.get(a) or not layout.get(b): continue
#                 if not PIPES.get(layout[a]) or not PIPES.get(layout[b]): continue
#                 pa, pb = PIPES[layout[a]], PIPES[layout[b]]
#                 if (-ai, -aj) in pa:
#                     if (-bi, -bj) in pb:
#                         graph[start].add(a)
#                         graph[start].add(b)
#                         graph[a].add(start)
#                         graph[b].add(start)   
#                         break
                    
#     # Traverse
#     nodes = {start}
#     visited = {}
#     depth = 0
#     while nodes:
#         next_nodes = set()
#         for node in nodes:
#             visited[node] = depth
#             next_nodes |= graph[node]
#         depth += 1
#         nodes = next_nodes - set(visited)
    
#     return max(visited.values())

            


    


