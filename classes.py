import random
from constants import STARTING_PLAYER_HP, SIZE

class EmptyTile:
    def __repr__(self):
        return "."

class Player:
    def __init__(self, name, hp, coords):
        self.name = name
        self.hp = hp
        self.coords = coords

    def __repr__(self):
        return self.name[0]

    @classmethod
    def inst(cls):
        return cls(cls.__name__, STARTING_PLAYER_HP, (random.randint(0, SIZE-1), random.randint(0, SIZE-1)))

    def on_turn(self):
        raise NotImplementedError()

    def on_hit(self):
        raise NotImplementedError()

    def on_signal(self):
        raise NotImplementedError()

class Signal:
    def __init__(self, direction, hp):
        self.direction = direction
        self.hp = hp

    def __repr__(self):
        return "@"

class Projectile:
    def __init__(self, direction, hp):
        self.direction = direction
        self.hp = hp

    def __repr__(self):
        return "X"
