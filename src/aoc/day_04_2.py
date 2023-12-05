if __name__ == "__main__":
    with open("inputs/day_04.txt") as f:
        rows = [row.strip() for row in f.readlines()]

    counts = [1] * len(rows)

    for i, row in enumerate(rows):
        data = row.split(":")[1]
        A, B = [set(int(val) for val in part.split()) for part in data.split("|")]
        matches = len(A & B)
        for j in range(i + 1, i + 1 + matches):
            counts[j] += counts[i]
    print(sum(counts))
