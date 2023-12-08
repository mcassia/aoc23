from utils import get_input_lines
import math
from functools import reduce


lcm = lambda values: reduce(lambda a, b: abs(a*b) // math.gcd(a, b), values)


def solve_1():

    lines = get_input_lines()

    # Convert the 'L' and 'R' instructions into 0 and 1 to quickly access the pairs
    instructions = [{'L': 0, 'R': 1}[c] for c in lines[0]]

    # Parse the map
    m = {}
    for line in lines[2:]:
        node, options = line.split(' = ')
        options = options[1:-1].split(', ')
        m[node] = options

    # Walk
    node = 'AAA'
    steps = 0
    while node != 'ZZZ':
        node = m[node][instructions[steps % len(instructions)]]
        steps += 1

    return steps


def solve_2():

    lines = get_input_lines()

    # Convert the 'L' and 'R' instructions into 0 and 1 to quickly access the pairs
    instructions = [{'L': 0, 'R': 1}[c] for c in lines[0]]

    # Parse the map
    m = {}
    for line in lines[2:]:
        node, options = line.split(' = ')
        options = options[1:-1].split(', ')
        m[node] = options

    # For each starting node, determine the walking period, that is, the sequence that repeats to
    # infinity when following the instructions for the given map and starting node
    starting_nodes = [node for node in m if node.endswith('A')]
    end_indices, periods = [], []
    for starting_node in starting_nodes:
        node = starting_node
        visited = set()
        end_indices_ = []
        steps = 0
        i = 0
        while (node, i) not in visited:
            visited.add((node, i))
            node = m[node][instructions[i]]
            steps += 1
            i = steps % len(instructions)
            if node.endswith('Z'):
                end_indices_.append(steps)
        periods.append(steps)
        end_indices.append(end_indices_)

    # Given the number of steps required to reach the end node for each start node, the first step
    # at which they all are at the end node at the same time is the least common multiplier of the
    # number of steps required for each starting node; this is possible because for each start node
    # it is the case that the number of steps required to reach the end node is also the period
    # length.

    return lcm([x[0] for x in end_indices])