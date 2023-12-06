from utils import get_input_lines


def solve_1():
    
    seeds, maps = parse()

    results = []
    
    for seed in seeds:
        value = seed
        for ranges in maps:
            value = run(value, ranges)
        results.append(value)

    return min(results)


def solve_2():
    
    # Parse the input
    seeds, maps = parse()
    seed_ranges = [
        (seeds[i*2], seeds[1+i*2])
        for i in range(len(seeds) // 2)
    ]
    minimum = None

    # For each seed range
    for _start, _length in seed_ranges:

        # To track the values through the mappings
        current_seed_ranges = {(_start, _length)}
        next_seed_ranges = set()

        # For each mapping
        for ranges in maps:

            # For each sub seed range
            for start, length in current_seed_ranges:

                # Split the seed range into multiple, according to the map, such that each sub-seed
                # range is linked to at most one map
                end = start + length
                pivots = sorted({
                    pivot
                    for _, source, length in ranges
                    for pivot in (source, source + length)
                    if start < pivot < end
                })
                pivots = [start, *pivots, end]
                split_seed_ranges = []
                for i in range(len(pivots) - 1):
                    split_seed_ranges.append((pivots[i], pivots[i+1]))

                # Update the seed ranges
                for s, e in split_seed_ranges:
                    for destination, source, delta in ranges:
                        if source <= s < source + delta:
                            next_seed_ranges.add((s + destination - source, e - s))
                            break
                    else:
                        next_seed_ranges.add((s, e - s))

            current_seed_ranges = next_seed_ranges
            next_seed_ranges = set()

        n = min({a for a, _ in current_seed_ranges})
        if minimum is None or n <= minimum:
            minimum = n

    return minimum



def run(n, ranges):
    """Evaluates the given number against the given ranges to find the resulting value"""
    for destination, source, length in ranges:
        if source <= n < source + length:
            return destination + n - source
    return n


def parse():
    lines = get_input_lines()
    seeds = tuple(map(int, lines[0].split(': ')[1].split()))
    maps = []
    for line in lines[2:]:
        if not line:
            continue
        elif 'map' in line:
            maps.append([])
        else:
            maps[-1].append(tuple(map(int, line.split())))

    return seeds, maps