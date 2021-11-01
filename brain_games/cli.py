#!/usr/bin/env python3.


import prompt


def weclome_user():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def intro():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def correct_answer():
    print('Correct!')


def wrong_answer(user_answer, correct, name):
    print('\'{}\' is wrong answer ;(. Correct answer was \'{}\''.format(user_answer, correct))
    print('Let\'s try again, {}!'.format(name))

 
def congrats(name):
    print('Congratulations, {}!'.format(name))