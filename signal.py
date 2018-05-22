import random
from classes import *
from constants import SIZE, STARTING_SIGNAL_HP
from submissions import players

def format_map(map_):
    return "\n".join(map("".join, map(lambda x: map(str, x), map_)))

def generate_y(idx_y):
    y = []
    for idx_x in range(SIZE):
        if any([x.coords == (idx_x, idx_y) for x in copy]):
            player = [x for x in copy if x.coords == (idx_x, idx_y)][0]
            copy.remove(player)
            y.append(player)
        else:
            y.append(EmptyTile())
    return y

if __name__ == "__main__":
    copy = players.copy()
    map_ = list(map(generate_y, range(SIZE)))
    print(format_map(map_))
    while True:
        for player in players:
            player.on_turn()
