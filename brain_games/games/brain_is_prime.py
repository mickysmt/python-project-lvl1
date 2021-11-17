#!/usr/bin/env python3.

from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    divider = 2
    if num < 2:
        return False
    while divider <= num / 2:
        if num % divider == 0:
            return False
        divider += 1
    return True


def generate_round():
    number = randint(1, 100)
    question = ('Question: ' + str(number))
    if is_prime(number) is True:
        correct = 'yes'
    else:
        correct = 'no'
    return(correct, question)
