def make_mapper(chunk):
    mapper = {}
    for row in chunk.split("\n")[1:]:
        dest_start, source_start, window = [int(val) for val in row.split()]
        for i in range(window):
            mapper[source_start + i] = dest_start + i
    return mapper


if __name__ == "__main__":
    with open("inputs/day_05.txt") as f:
        chunks = f.read().split("\n\n")
    seeds = [int(val) for val in chunks.pop(0).split()[1:]]
    for chunk in chunks:
        mapper = make_mapper(chunk)
        seeds = [mapper.get(seed, seed) for seed in seeds]
