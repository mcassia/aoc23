from utils import get_input_lines


def solve(layout, initial_beam):

    # Initialize, by fetching size of the layout and sets to track visited (locations, directions)
    # of beams
    height, width = len(layout), len(layout[0])
    visited = set()
    beams = {initial_beam}

    # While there are beams to move forward
    while beams:
        next_beams = set()
        for beam in beams:
            if beam in visited: continue
            visited.add(beam)

            # Determine the beam's next location and direction, if any
            i, j, di, dj = beam
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                c = layout[ni][nj]
                if c == '.':
                    next_beams.add((ni, nj, di, dj))
                elif c == '\\':
                    next_beams.add((ni, nj, dj, di))
                elif c == '/':
                    next_beams.add((ni, nj, -dj, -di))
                elif c == '-':
                    if di == 0:
                        next_beams.add((ni, nj, di, dj))
                    else:
                        next_beams.add((ni, nj, 0, 1))
                        next_beams.add((ni, nj, 0, -1))
                elif c == '|':
                    if dj == 0:
                        next_beams.add((ni, nj, di, dj))
                    else:
                        next_beams.add((ni, nj, 1, 0))
                        next_beams.add((ni, nj, -1, 0))
        
        beams = next_beams
    
    visited.remove(initial_beam)
    locations = {(i, j) for i, j, _, _ in visited}

    return len(locations)


def solve_1():

    layout = [list(line) for line in get_input_lines()]
    
    # Start to the left of the top-left corner, moving rightwards
    return solve(layout, (0, -1, 0, 1))


def solve_2():

    layout = [list(line) for line in get_input_lines()]
    height, width = len(layout), len(layout[0])

    # Determine every possible start location i.e. right outside the layout, pointing to the layout
    beams = set()
    
    for i in range(height):
        beams.add((i, -1, 0, 1))
        beams.add((i, width, 0, -1))

    for j in range(width):
        beams.add((-1, j, 1, 0))
        beams.add((height, j, -1, 0))

    return max(solve(layout, beam) for beam in beams)

    
                        

