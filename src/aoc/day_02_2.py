from dataclasses import dataclass, field


@dataclass
class Round:
    red: int = 0
    blue: int = 0
    green: int = 0


@dataclass
class Game:
    id: int
    rounds: list[Round] = field(default_factory=list)


def parse_input(path):
    games = []
    with open(path) as f:
        for line in f.readlines():
            name, data = line.strip().split(": ")
            game_id = int(name.split()[-1])
            games.append(Game(id=game_id))
            for round_ in data.split("; "):
                round_data = dict()
                for pair in round_.split(", "):
                    count, colour = pair.split(" ")
                    round_data[colour] = int(count)
                games[-1].rounds.append(Round(**round_data))
    return games


def is_valid(game: Game, constraints) -> bool:
    for colour, count in constraints.items():
        for round_ in game.rounds:
            if getattr(round_, colour) > count:
                return False
    return True


COLOURS = ("red", "green", "blue")
CONSTRAINTS = {"red": 12, "green": 13, "blue": 15}


def find_min_cubes(game):
    return {colour: max(getattr(round_, colour) for round_ in game.rounds) for colour in COLOURS}


def power(round_: Round):
    return round_.red * round_.blue * round_.green

if __name__ == "__main__":
    games = parse_input("inputs/day_02.txt")
    print(sum([power(Round(**find_min_cubes(game))) for game in games]))