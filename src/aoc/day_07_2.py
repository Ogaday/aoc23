from collections import Counter
from dataclasses import dataclass
from functools import cached_property, reduce
from string import digits
from typing import Any

strengths = {
    **{i: int(i) for i in digits},
    **{"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14},
}


@dataclass(frozen=True)
class Card:
    """
    >>> Card(5) == Card(5)
    True
    >>> Card(5) <= Card(5)
    True
    >>> Card(5) >= Card(5)
    True
    >>> Card(5) > Card(4)
    True
    >>> Card(5) < Card(6)
    True
    >>> sorted([Card(val) for val in "AKQJT9"])
    [Card(value='J'), Card(value='9'), Card(value='T'), Card(value='Q'), Card(value='K'), Card(value='A')]
    """

    value: str

    @property
    def strength(self) -> int:
        return strengths.get(self.value, self.value)

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Card):
            return self.strength < other.strength
        raise TypeError

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Card):
            return self.strength <= other.strength
        raise TypeError


@dataclass
class Hand:
    cards: tuple[Card, Card, Card, Card, Card]
    bid: int

    @cached_property
    def tricks(self):
        counts = Counter(self.cards)
        num_jokers = counts.pop(Card("J"), 0)
        if num_jokers == 5:
            return (5,)
        best_trick, _ = counts.most_common(1)[0]
        counts[best_trick] += num_jokers
        return tuple(count for _, count in counts.most_common())

    def __lt__(self, other: Any):
        if isinstance(other, Hand):
            return (self.tricks, self.cards) < (other.tricks, other.cards)
        raise TypeError()

    def __le__(self, other: Any):
        if isinstance(other, Hand):
            return (self.tricks, self.cards) <= (other.tricks, other.cards)
        raise TypeError()


if __name__ == "__main__":
    hands = []
    with open("inputs/day_07.txt") as f:
        for line in f.readlines():
            cards, bid = line.split()
            hands.append(Hand(cards=tuple(Card(val) for val in cards), bid=int(bid)))

    print(
        sum(
            [
                rank * hand.bid
                for hand, rank in zip(sorted(hands), range(1, len(hands) + 1))
            ]
        )
    )
