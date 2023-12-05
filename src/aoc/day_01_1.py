from string import digits


def get_calibration_value(row: str) -> int:
    numbers = [char for char in row if char in digits]
    return int(numbers[0] + numbers[-1])


def solution(path) -> int:
    """
    >>> solution
    """
    with open(path) as f:
        solution = sum(get_calibration_value(line.strip()) for line in f.readlines())
    return solution


if __name__ == "__main__":
    solution("inputs/day_01.txt")
