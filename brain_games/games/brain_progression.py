#!/usr/bin/env python3.

from random import randint, choice
from brain_games.games.game_engine import engine, random_num


def make_progression():
    first_num = random_num()
    delta = randint(1, 20)
    prog_length = 10
    last_num = (delta * prog_length) + first_num
    return range(first_num, last_num, delta)


def game_logic():
    prog = make_progression()
    correct = choice(prog)
    quest_prog = ' '.join(['..' if i == correct else str(i) for i in prog])
    question = ('Question: ' + quest_prog)
    return(str(correct), question)


def game():
    engine(game_logic)
