from utils import get_input_lines


def solve_1():
    return _solve(expansion_factor=2)


def solve_2():
    return _solve(expansion_factor=1_000_000)


def _solve(expansion_factor):

    # Parse and determine the expansion rows and columns
    layout = get_input_lines()
    rows, columns = {}, {}
    for i, row in enumerate(layout):
        for j, c in enumerate(row):
            rows[i] = rows.get(i, set()) | {c}
            columns[j] = columns.get(j, set()) | {c}
    rows = {row for row, cs in rows.items() if cs == {'.'}}
    columns = {column for column, cs in columns.items() if cs == {'.'}}

    # Detect the galaxies
    galaxies = set()
    for i, row in enumerate(layout):
        for j, c in enumerate(row):
            if c == '#':
                galaxies.add((i, j))
    galaxies = sorted(galaxies)

    # Traverse all distinct pairs of galaxies
    distances = {}
    for i, g1 in enumerate(galaxies):
        for j, g2 in enumerate(galaxies):
            k = tuple(sorted([i, j]))
            if i != j and k not in distances:

                # Determine the shorted distance (manhattan)
                distance = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

                # Determine the 'big' rows and columns crossed
                count = (
                    len(set(range(*sorted([g1[0], g2[0]]))).intersection(rows))
                    +
                    len(set(range(*sorted([g1[1], g2[1]]))).intersection(columns))
                )

                # 'Replace' the size of the steps on 'big' rows and columns
                distance += count * (expansion_factor - 1)
                distances[k] = distance

    return sum(distances.values())