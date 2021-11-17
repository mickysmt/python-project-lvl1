#!/usr/bin/env python3.

from random import randint

RULE = 'Find the greatest common divisor of given numbers.'


def gcd(num_one, num_two):
    if num_two == 0:
        return num_one
    return gcd(num_two, num_one % num_two)


def generate_round():
    num_one = randint(1, 100)
    num_two = randint(1, 100)
    correct = gcd(num_one, num_two)
    question = ('Question: ' + str(num_one) + ' ' + str(num_two))
    return(correct, question)
