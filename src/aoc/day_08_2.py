from itertools import cycle
import math

if __name__ == "__main__":
    graph = {}
    with open("inputs/day_08.txt") as f:
        instructions = f.readline().strip()
        f.readline()
        for line in f.readlines():
            node, adjacents = line.strip().split(" = ")
            left, right = [node.strip(")").strip("(") for node in adjacents.split(", ")]
            graph[node] = left, right
    nodes = [node for node in graph if node.endswith("A")]
    solutions = {node: [] for node in nodes}
    directions = {"L": 0, "R": 1}
    for initial_node in nodes:
        print(f"starting at {initial_node}")
        node = initial_node
        seen = set()
        for steps, (i, inst) in enumerate(cycle(enumerate(instructions))):
            if i == 0:
                print("starting...")
            node = graph[node][directions[inst]]
            if node.endswith("Z"):
                print(f"found {node}")
                solutions[initial_node].append(steps + 1)
            if (node, i) in seen:
                break
            seen.add((node, i))
    print(math.lcm(*[sol[0] for sol in solutions.values()]))
