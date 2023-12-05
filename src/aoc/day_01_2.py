from string import digits


replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def apply_substitutions(row, map):
    for old, new in map.items():
        row = row.replace(old, new)
    return row

def get_calibration_value(row: str) -> int:
    numbers = [char for char in row if char in digits]
    return int(numbers[0] + numbers[-1])


def solution(path) -> int:
    """
    >>> solution
    """
    with open(path) as f:
        solution = sum(get_calibration_value(apply_substitutions(line.strip(), map=replacements)) for line in f.readlines())
    return solution


if __name__ == "__main__":
    print(solution("inputs/day_01.txt"))