
from itertools import cycle


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
    steps = 0
    directions = {"L": 0, "R": 1}
    for inst in cycle(instructions):
        for i, node in enumerate(nodes):
            nodes[i] = graph[node][directions[inst]]
        steps += 1
        if all(node.endswith("Z") for node in nodes):
            break
    print(steps)
