import random

try:
    import pandas
except ImportError:
    pandas = None

def take_one(*args):
    return 1

def take_two(*args):
    return 2

def take_three(*args):
    return 3

def tit_for_tat(turn, round, fish, results, state):
    if results:
        values = list(results[-1].values())
        return max(set(values), key=values.count)
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

def exploit_meek(turn, round, fish, results, state):
    if results:
        values = list(results[-1].values())
        return 4 - max(set(values), key=values.count)
    else:
        return 3

def human_player(turn, round, fish, results, state):
    print(f"turn {turn}, round {round}, {fish} fish")
    print("======")
    if pandas:
        pretty_results = [{k.__name__: x[k] for k in x} for x in results]
        print(pandas.DataFrame(pretty_results).to_string())
    else:
        print(f"results: {results}")
    print("======")
    return int(input(">"))

players = [take_two, human_player]
[take_one, take_two, take_three, tit_for_tat, random_strategy, low_random, high_random, minimum_high_random, exploit_meek]
