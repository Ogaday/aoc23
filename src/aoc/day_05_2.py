from dataclasses import dataclass
from typing import Any, overload


class NoIntersectionError(Exception):
    ...


@dataclass
class Range:
    start: int
    stop: int

    def __and__(self, other: "Range") -> "Range":
        """
        >>> Range(3, 10) & Range(1, 5)
        Range(start=3, stop=5)
        >>> Range(1, 5) & Range(3, 10)
        Range(start=3, stop=5)
        >>> Range(1, 2) & Range(2, 3)
        Traceback (most recent call last):
            ...
        aoc.day_05_2.NoIntersectionError
        """
        if self.stop <= other.start or self.start >= other.stop:
            raise NoIntersectionError()
        return Range(max(self.start, other.start), min(self.stop, other.stop))

    def __add__(self, other):
        """
        >>> Range(3, 5) + 6
        Range(start=9, stop=11)
        >>> Range(3, 5) + Range(1, 2)
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for +: 'Range' and 'Range'
        """
        if isinstance(other, int):
            return Range(self.start + other, self.stop + other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: '{type(self).__name__}' "
                f"and '{type(other).__name__}'"
            )

    @overload
    def __sub__(self, other: int) -> "Range":
        ...

    @overload
    def __sub__(self, other: "Range") -> list["Range"]:
        ...

    def __sub__(self, other: Any):
        """
        >>> Range(5, 10) - Range(7, 8)
        [Range(start=5, stop=7), Range(start=8, stop=10)]
        >>> Range(5, 10) - Range(3, 5)
        [Range(start=5, stop=10)]
        >>> Range(5, 10) - Range(12, 15)
        [Range(start=5, stop=10)]
        >>> Range(5, 10) - Range(0, 15)
        []
        >>> Range(5, 10) - 3
        Range(start=2, stop=7)
        """
        if isinstance(other, Range):
            ret = []
            if self.start < other.start:
                ret.append(Range(self.start, min(self.stop, other.start)))
            if self.stop > other.stop:
                ret.append(Range(max(other.stop, self.start), self.stop))
            return ret
        elif isinstance(other, int):
            return Range(self.start - other, self.stop - other)
        else:
            raise TypeError(
                f"unsupported operand type(s) for -: '{type(self).__name__}' "
                f"and '{type(other).__name__}'"
            )

    def __lt__(self, other: Any) -> bool:
        return self.start < other.start


@dataclass
class RangeMap:
    source_range: Range
    offset: int

    @property
    def dest_range(self):
        return Range(
            self.source_range.start + self.offset, self.source_range.stop + self.offset
        )

    def apply(self, other: Range) -> Range:
        mapped = (self.source_range & other) + self.offset
        return mapped


@dataclass
class Mapper:
    maps: list[RangeMap]

    def apply(self, ranges: list[Range]) -> list[Range]:
        unmapped = []
        mapped = []
        for map in self.maps:
            for range in ranges:
                try:
                    mapped.append(map.apply(range))
                except NoIntersectionError:
                    pass
                unmapped += range - map.source_range
            ranges, unmapped = unmapped, []
        return mapped + ranges


def pairs(iterable):
    yield from zip(iterable[::2], iterable[1::2])


if __name__ == "__main__":
    with open("inputs/day_05.txt") as f:
        chunks = f.read().split("\n\n")
    seed_row = [int(val) for val in chunks.pop(0).split()[1:]]
    seed_ranges = []
    for start, length in pairs(seed_row):
        seed_ranges.append(Range(start=start, stop=start + length))

    mappers = []
    for chunk in chunks:
        mapper = Mapper([])
        for row in chunk.strip().split("\n")[1:]:
            dest_start, source_start, length = [int(val) for val in row.split()]
            mapper.maps.append(
                RangeMap(
                    source_range=Range(source_start, source_start + length),
                    offset=dest_start - source_start,
                )
            )
        mappers.append(mapper)
    new_seeds = seed_ranges
    for mapper in mappers:
        new_seeds = mapper.apply(new_seeds)
    print(min(new_seeds))
