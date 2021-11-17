#!/usr/bin/env python3.

from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    random_number = randint(1, 100)
    question = ('Question: ' + str(random_number))
    return ('no' if random_number % 2 else 'yes', question)
