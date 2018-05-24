#!/usr/bin/python3
# Controller for Fish and Chips

import constants
import submissions
import random

def add_dicts(original, delta):
    return {k: (v + delta[k]) if k in delta else v for k, v in original.items()}

def run_game(players):
    scores = {x: 0 for x in players}
    for _ in range(constants.RUNS):
        if constants.GROUP_SIZE:
            # randomly group into groups of constants.GROUP_SIZE
            random.shuffle(players)
            groups = [players[x:x+constants.GROUP_SIZE]
                     if len(players) > x+constants.GROUP_SIZE
                     else players[x:]
                     for x in 
                     range(0, len(players), constants.GROUP_SIZE)]
            for group in groups:
                delta_scores = run_permutation(group.copy())
                scores = add_dicts(scores, delta_scores)
        else:
            delta_scores = run_permutation(players.copy())
            scores = add_dicts(scores, delta_scores)
    return scores

def run_permutation(players):
    fish = int(len(players) * constants.FISH_MULTIPLIER)
    states = {x: {} for x in players}
    scores = {x: 0 for x in players}
    for i in range(constants.STARTING_NEED, constants.ROUND_LIMIT):
        round_results = []
        turn = 1
        fish_eaten = {x: 0 for x in players}
        while fish:
            turn_results = {x: 0 for x in players}
            requests = {}
            random.shuffle(players)
            for player in players:
                requests[player] = player(turn, i, fish, round_results, states[player])
                if requests[player] > 3:
                    raise Exception("function requested more than three fish")

            while requests:
                new_requests = requests.copy()
                for request in requests:
                    if requests[request] and fish:
                        new_requests[request] -= 1
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
    scores = run_game(submissions.players)
    for k in sorted(scores, key=scores.get, reverse=True):
         print(f"{k.__name__} scored {scores[k]}")
