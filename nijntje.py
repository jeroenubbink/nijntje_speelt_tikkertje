from enum import Enum
from itertools import cycle
import random

class Player(Enum):
    NIJNTJE = 0
    KNORRETJE = 1
    NINA = 2
    SNUF = 3

BOARD = [
    Player.NIJNTJE,
    Player.KNORRETJE,
    Player.NINA,
    Player.SNUF,
    Player.NIJNTJE,
    Player.NINA,
    Player.SNUF,
    Player.KNORRETJE,
    Player.SNUF,
    Player.NINA,
    Player.NIJNTJE,
    Player.KNORRETJE,
    Player.SNUF,
    Player.NINA,
    Player.NIJNTJE,
    Player.KNORRETJE,
    Player.SNUF,
    Player.NINA,
    Player.NIJNTJE,
    Player.SNUF,
    Player.KNORRETJE,
    Player.NIJNTJE,
    Player.NINA,
    Player.SNUF,
    Player.KNORRETJE,
    Player.NIJNTJE,
    Player.KNORRETJE,
    Player.NINA,
    Player.SNUF,
    Player.NIJNTJE,
    Player.KNORRETJE,
    Player.NIJNTJE,
    Player.SNUF,
    Player.NINA,
    Player.NIJNTJE,
    Player.KNORRETJE,
    Player.NINA,
    Player.SNUF,
    Player.KNORRETJE,
    Player.NIJNTJE,
]

def show_stats():
    print(f"Statistics after {count} iterations:\n\n")
    for player in Player:
        print(f"{player.name:<10}:  wins: {win[player.value]:>10} = {win[player.value]/count*100}%")
    print("\n\n")

win = [0, 0, 0, 0]

count = 1

try:
    while(True):
        positions = [0, 0, 0, 0]
        starter = random.choice(list(Player))
        player_cycle = cycle(Player)
        current_player = next(player_cycle)

        while not(current_player == starter):
            current_player = next(player_cycle)

        while not(any(position > len(BOARD) for position in positions)):
            positions[current_player.value] += random.randrange(1,6)
            try:
                if not(BOARD[positions[current_player.value]] == Player(current_player)):
                    current_player = next(player_cycle)
            except IndexError:
                # player already won
                pass

        winner = max(positions)
        winner_index = [index for index, value in enumerate(positions) if value == winner][0]
        win[winner_index] += 1

        if(count % 10000 == 0):
            show_stats()

        count += 1

except KeyboardInterrupt:
    pass

show_stats()
