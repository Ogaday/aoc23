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


def get_calibration_value(row: str) -> int:
    values = parse_row(row)
    return int(values[0] + values[-1])


def parse_row(row: str) -> list[str]:
    values = []
    for i in range(len(row)):
        if row[i] in digits:
            values.append(row[i])
        else:
            for key, value in replacements.items():
                if row[i:].startswith(key):
                    values.append(value)
                    break
    return values


def solution(path) -> int:
    """
    >>> solution
    """
    with open(path) as f:
        solution = sum(get_calibration_value(line.strip()) for line in f.readlines())
    return solution


if __name__ == "__main__":
    print(solution("inputs/day_01.txt"))
