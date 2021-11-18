#!/usr/bin/env python3.

import operator
from random import choice, randint

RULE = 'What is the result of the expression?'


ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}


def calculate_correct_answer(num_one, num_two, exp):
    correct_answer = (ops[exp](num_one, num_two))
    return correct_answer


def generate_round():
    num_one = randint(1, 100)
    num_two = randint(1, 100)
    exp = choice(list(ops.keys()))
    correct = calculate_correct_answer(num_one, num_two, exp)
    question = str(num_one) + ' ' + exp + ' ' + str(num_two)
    return(correct, question)
