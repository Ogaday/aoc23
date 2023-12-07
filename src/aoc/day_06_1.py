import math
from functools import reduce


class ImaginaryRootsError(Exception):
    ...


def quadratic(a: int, b: int, c: int) -> tuple[float, float]:
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        raise ImaginaryRootsError(f"Quadratic {a}x^2 + {b}x + {c} has no real roots.")
    return (
        (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a),
        (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a),
    )


def winning_times(time: int, distance) -> int:
    lb, ub = quadratic(-1, time, -distance)
    if (min_seconds := math.ceil(lb)) == lb:
        min_seconds += 1
    if (max_seconds := math.floor(ub)) == ub:
        max_seconds -= 1

    return max_seconds - min_seconds + 1


if __name__ == "__main__":
    with open("inputs/day_06.txt") as f:
        times, distances = [
            [int(val) for val in row.split()[1:]] for row in f.readlines()
        ]
    ways_to_win = [
        winning_times(time, distance) for time, distance in zip(times, distances)
    ]
    print(reduce(int.__mul__, ways_to_win, 1))
