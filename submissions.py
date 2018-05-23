import statistics
import random

def take_one(*args):
    return 1

def take_two(*args):
    return 2

def take_three(*args):
    return 3

def tit_for_tat(turn, round, fish, results, state):
    if results:
        return statistics.mode(list(results[-1].values()))
    else:
        return 1

def random_strategy(*args):
    return random.choice([1,2,3])
    
def low_random(*args):
    return random.choice([1,1,1,2,2,3])

def high_random(*args):
    return random.choice([1,2,2,3,3,3])

def minimum_high_random(turn, round, fish, results, state):
    if round == 1:
        return 1
    elif round == 2:
        return random.choice([1,2,2])
    else:
        return random.choice([1,2,2,3,3,3])

players = [take_one, take_two, take_three, tit_for_tat, random_strategy, low_random, high_random, minimum_high_random]
