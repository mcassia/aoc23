from utils import get_input_lines


def solve_2():

    # Parse and determine the expansion rows and columns
    layout = get_input_lines()
    height, width = len(layout), len(layout[0])
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

    # Determine all distances between each pair of galaxies and consider the 'big' rows and
    # 'columns' they have to traverse
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
                distance += count * (1_000_000 - 1)
                distances[k] = distance

    return sum(distances.values())


def solve_1():

    # Parse and expand the universe
    layout = get_input_lines()
    height, width = len(layout), len(layout[0])
    rows, columns = {}, {}
    for i, row in enumerate(layout):
        for j, c in enumerate(row):
            rows[i] = rows.get(i, set()) | {c}
            columns[j] = columns.get(j, set()) | {c}
    rows = {row for row, cs in rows.items() if cs == {'.'}}
    columns = {column for column, cs in columns.items() if cs == {'.'}}
    for i in reversed(sorted(rows)):
        layout.insert(i, ['.' for _ in range(width)])
    for i, row in enumerate(layout):
        new_row = list(row)
        for j in reversed(sorted(columns)):
            new_row.insert(j, '.')
        layout[i] = new_row

    # Detect the galaxies
    galaxies = set()
    for i, row in enumerate(layout):
        for j, c in enumerate(row):
            if c == '#':
                galaxies.add((i, j))
    galaxies = sorted(galaxies)

    # Determine all distances
    distances = {}
    for i, g1 in enumerate(galaxies):
        for j, g2 in enumerate(galaxies):
            k = tuple(sorted([i, j]))
            if i != j and k not in distances:
                distance = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
                distances[k] = distance

    return sum(distances.values())

