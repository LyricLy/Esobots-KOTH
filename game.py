#!/usr/bin/python3
# Controller for Fish and Chips

import constants
import submissions
import random
from collections import Counter

def counter():
    i = constants.STARTING_NEED
    while True:
        yield i
        i += 1

def run_game(players):
    fish = int(len(players) * constants.FISH_MULTIPLIER)
    states = {x: {} for x in players}
    scores = {x: 0 for x in players}
    for i in range(1, constants.ROUND_LIMIT):
        round_results = []
        turn = 1
        fish_eaten = {x: 0 for x in players}
        while fish:
            turn_results = {x: 0 for x in players}
            requests = {}
            random.shuffle(players)
            for player in players:
                requests[player] = player(turn, i, fish, round_results, states[player])

            while requests:
                new_requests = requests.copy()
                for request in requests:
                    if requests[request] and fish:
                        requests[request] -= 1
                        fish -= 1
                        turn_results[request] += 1
                        fish_eaten[request] += 1
                    else:
                        new_requests.pop(request)
                requests = new_requests

            round_results.append(turn_results)
            fish += fish // 2
            if turn == constants.TURN_LIMIT:
                break
            turn += 1

            for player in players:
                if fish_eaten[player] < i:
                    break
            else:
                break
        else:
            for player in players:
                if fish_eaten[player] < i:
                    players.remove(player)
                    scores[player] = i
        if len(players) == 1:
            scores[players[0]] = 100
            players = []
            break
    for player in players:
        scores[player] = 100
    return scores

if __name__ == "__main__":
    scores = {x: 0 for x in submissions.players}
    for _ in range(constants.RUNS):
        scores = dict(Counter(scores) + Counter(run_game(submissions.players.copy())))
    print(scores)
