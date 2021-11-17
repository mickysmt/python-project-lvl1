#!/usr/bin/env python3.

from random import randint, choice

RULE = 'What number is missing in the progression?'

PROGESSION_LENGTH = 10


def generate_first_num():
    return randint(1, 100)


def generate_delta():
    return randint(1, 20)


def generate_progression():
    first_num = generate_first_num()
    delta = generate_delta()
    last_num = (delta * PROGESSION_LENGTH) + first_num
    return range(first_num, last_num, delta)


def generate_round():
    prog = generate_progression()
    correct = choice(prog)
    quest_prog = ' '.join(['..' if i == correct else str(i) for i in prog])
    question = ('Question: ' + quest_prog)
    return(str(correct), question)
