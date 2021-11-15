#!/usr/bin/env python3.


import operator
from random import choice
from brain_games.games.game_engine import engine, random_num


ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def game_logic():
    num_one = random_num()
    num_two = random_num()
    exp = choice(list(ops.keys()))
    correct = (ops[exp](num_one, num_two))
    question = ('Question: ' + str(num_one) + ' ' + exp + ' ' + str(num_two))
    return(correct, question)


def game():
    engine(game_logic)
