from string import digits
from itertools import product
from collections import namedtuple
class Vector(namedtuple("Vector", ["X", "Y"])):
    def __add__(self, other: "Vector"):
        return Vector(self.X + other.X, self.Y + other.Y)
    def __sub__(self, other: "Vector"):
        return Vector(self.X - other.X, self.Y - other.Y)
    

def get_neighbours(x: Vector):
    for i, j in product(range(-1, 2), range(-1, 2)):
        yield x + Vector(i, j)


def parse_input(rows: list[str]) -> tuple[dict[Vector, str], dict[tuple[Vector], int]]:
    symbols = {}
    numbers = {}
    for y, row in enumerate(rows):
        stack = []
        for x, char in enumerate(row):
            if char in digits:
                stack.append((char, Vector(x, y)))
                # Skip stack check
                continue
            elif char == ".":
                pass
            else:
                # Is symbol
                symbols[Vector(x, y)] = char
            if stack:
                numbers[tuple(vec for num, vec in stack)] = int("".join(num for num, vec in stack))
                stack = []
        if stack:
            numbers[tuple(vec for num, vec in stack)] = int("".join(num for num, vec in stack))
            stack = []
        
    return symbols, numbers

def is_match(vec, number):
    return bool(set(get_neighbours(vec)) & set(number))


def solution(path):
    with open(path) as f:
        rows = [row.strip() for row in f.readlines()]
    symbols, numbers = parse_input(rows)
    regions = set.union(*[set(get_neighbours(vec)) for vec in symbols.keys()])
    stars = {vec for vec, symbol in symbols.items() if symbol == "*"}
    possible_gears = {star: [num for vecs, num in numbers.items() if is_match(star, vecs)] for star in stars}
    gears = [value for key, value in possible_gears.items() if len(value) == 2]
    return sum(a * b for a, b in gears)

if __name__ == "__main__":
    print(solution("inputs/day_03.txt"))