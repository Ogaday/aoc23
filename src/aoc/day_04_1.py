if __name__ == "__main__":
    with open("inputs/day_04.txt") as f:
        rows = [row.strip() for row in f.readlines()]

    scores = []
    for row in rows:
        data = row.split(":")[1]
        A, B = [set(int(val) for val in part.split()) for part in data.split("|")]
        if matches := A & B:
            scores.append(2 ** (len(matches) - 1))
    print(sum(scores))