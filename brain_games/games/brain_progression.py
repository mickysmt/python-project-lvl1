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
    progression = make_progression()
    correct = choice(progression)
    prog_for_question = ' '.join(['..' if i == correct else str(i) for i in progression])
    question = ('Question: ' + prog_for_question)
    return(str(correct), question)


def game():
    engine(game_logic)
