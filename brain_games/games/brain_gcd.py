#!/usr/bin/env python3.

from brain_games.games.game_engine import engine, random_num


def gcd(num_one, num_two):
    if num_two == 0:
        return num_one
    return gcd(num_two, num_one % num_two)


def game_logic():
    num_one = random_num()
    num_two = random_num()
    correct = gcd(num_one, num_two)
    question = ('Question: ' + str(num_one) + ' ' + str(num_two))
    return(correct, question)


def game():
    engine(game_logic)
