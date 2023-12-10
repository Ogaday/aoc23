
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
    steps = ['AAA']
    directions = {"L": 0, "R": 1}
    for inst in cycle(instructions):
        steps.append(graph[steps[-1]][directions[inst]])
        if steps[-1] == "ZZZ":
            break
    print(len(steps) - 1)
