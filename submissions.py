import statistics

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

players = [take_one, take_two, take_three, tit_for_tat]
