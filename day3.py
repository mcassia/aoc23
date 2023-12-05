from utils import get_input_lines


def solve_1():

    engine = get_input_lines()
    height, width = len(engine), len(engine[0])

    # Find numbers and their locations in the engine schematic
    numbers = []
    for i, row in enumerate(engine):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                length = 1
                for k in row[j+1:]:
                    if k.isdigit():
                        length += 1
                    else:
                        break
                numbers.append((i, j, row[j:j+length]))
                j += length
            else:
                j += 1

    # Find numbers near symbols
    total = 0
    for i, j, number in numbers:
        near_symbol = False
        for d in range(len(number)):
            ai, aj = i, j + d
            for di in (-1, 0, +1):
                for dj in (-1, 0, +1):
                    ni, nj = ai + di, aj + dj
                    if 0 <= ni < height and 0 <= nj < width:
                        c = engine[ni][nj]
                        if not c.isdigit() and c != '.':
                            near_symbol = True # ideally break
        if near_symbol:
            total += int(number)        

    return total


def solve_2():

    engine = get_input_lines()
    height, width = len(engine), len(engine[0])

    # Find numbers and their locations in the engine schematic
    numbers = []
    for i, row in enumerate(engine):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                length = 1
                for k in row[j+1:]:
                    if k.isdigit():
                        length += 1
                    else:
                        break
                numbers.append((i, j, row[j:j+length]))
                j += length
            else:
                j += 1

    # Find numbers close to gears
    gears = {}
    for i, j, number in numbers:
        near_symbol = False
        for d in range(len(number)):
            ai, aj = i, j + d
            for di in (-1, 0, +1):
                for dj in (-1, 0, +1):
                    ni, nj = ai + di, aj + dj
                    if 0 <= ni < height and 0 <= nj < width:
                        c = engine[ni][nj]
                        if c == '*':
                            gears[(ni, nj)] = gears.get((ni, nj), set()) | {(i, j, number)}
        
    # Find the gear ratio result
    total = 0
    for gear, numbers in gears.items():
        if len(numbers) == 2:
            actual_numbers = [int(n) for _, _, n in numbers]
            total += actual_numbers[0] * actual_numbers[1]

    return total
        


