#!/usr/bin/env python3.

from random import randint, choice

RULE = 'What number is missing in the progression?'

PROGESSION_LENGTH = 10


def generate_progression(first_num, delta):
    last_num = (delta * PROGESSION_LENGTH) + first_num
    return range(first_num, last_num, delta)


def generate_round():
    first_num = randint(1, 100)
    delta = randint(1, 20)
    prog = generate_progression(first_num, delta)
    correct = choice(prog)
    question = ' '.join(['..' if i == correct else str(i) for i in prog])
    return(str(correct), question)
