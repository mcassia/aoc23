from utils import get_input_lines  


def solve_1():
    return solve(0, 3)


def solve_2():
    return solve(4, 10)


def solve(
        minimum_number_of_steps_in_direction,
        maximum_number_of_steps_in_direction,
    ):

    # Parse the input, generate the grid layout and determine the target
    lines = get_input_lines()
    layout = {
        (i, j): int(c)
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    }
    target = (len(lines)-1, len(lines[0])-1)

    paths = {((0, 0),)}
    scores = {} # (location, direction) -> minimum weight e.g. (17, 42) -> 31

    step = 0
    while paths:

        next_paths = set()
        for path in paths:
            
            # Determine the current direction and score
            i, j = path[-1]
            (pdi, pdj), pdc = get_direction(path)
            score = get_score(layout, path)

            # If the current node, in this direction and the number of steps in  the direction has
            # been encountered before, determine if it's worth continuing
            key = (i, j, pdi, pdj, pdc)
            if key in scores:
                if score < scores[key]: scores[key] = score
                else: continue
            else: scores[key] = score

            # Do not continue if it's the end node
            if (i, j) == target:
                continue

            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:

                # If this would be the 4th step in the same direction, do not continue
                if pdc != 0:
                    if (pdi, pdj) == (di, dj) and pdc >= maximum_number_of_steps_in_direction: continue
                    if (pdi, pdj) != (di, dj) and pdc < minimum_number_of_steps_in_direction: continue

                # Check if the neighbour in this direction is valid and if it's not the same as one
                # position ago
                ni, nj = i + di, j + dj
                if (ni, nj) not in layout: continue
                if len(path) > 1 and (ni, nj) == path[-2]: continue

                next_paths.add((*path, (ni, nj)))

        paths = next_paths
        step += 1

    scores = {
        node: min(v for k, v in scores.items() if k[:2] == node)
        for node in layout
    }

    return scores[target]


def get_score(layout, path):
    return sum(layout[p] for p in path[1:])


def get_direction(path):
    d, c = None, 0
    for i in range(len(path)-1):
        p1, p2 = path[-i-1], path[-i-2]
        di, dj = p1[0] - p2[0], p1[1] - p2[1]
        if d is None: d = (di, dj)
        if (di, dj) == d: c += 1
        else: return d, c
    return d or (None, None), c


