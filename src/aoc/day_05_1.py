from dataclasses import dataclass
from typing import Any


@dataclass
class RangeSpec:
    source_start: int
    dest_start: int
    length: int

    @property
    def source_end(self):
        return self.source_start + self.length

    def dest_end(self):
        return self.dest_start + self.length

    def __contains__(self, item: Any) -> bool:
        return self.source_start <= item < self.source_end

    def map(self, item: int) -> int:
        if item in self:
            offset = item - self.source_start
            return self.dest_start + offset
        raise KeyError(item)


class Mapper:
    def __init__(self, ranges: list[RangeSpec]):
        self.ranges = ranges

    def map(self, item: int) -> int:
        for spec in self.ranges:
            if item in spec:
                mapped = spec.map(item)
                break
        else:
            mapped = item
        return mapped


if __name__ == "__main__":
    with open("inputs/day_05.txt") as f:
        chunks = f.read().split("\n\n")
    seeds = [int(val) for val in chunks.pop(0).split()[1:]]
    mappers = []
    for chunk in chunks:
        specs = []
        for row in chunk.strip().split("\n")[1:]:
            dest_start, source_start, window = [int(val) for val in row.split()]
            specs.append(
                RangeSpec(
                    source_start=source_start, dest_start=dest_start, length=window
                )
            )
        mappers.append(Mapper(ranges=specs))
    new_seeds = seeds
    for mapper in mappers:
        new_seeds = [mapper.map(seed) for seed in new_seeds]
    print(min(new_seeds))
