#!/usr/bin/env python3.

from random import randint
import prompt

name = ''


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def calc_question():
    print('What is the result of the expression?')


def intro():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def correct_answer():
    print('Correct!')


def wrong_answer(user_answer, correct, name):
    print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, correct))
    print("Let's try again, {}!".format(name))


def congrats(name):
    print('Congratulations, {}!'.format(name))


def random_num():
    return randint(1, 10)
