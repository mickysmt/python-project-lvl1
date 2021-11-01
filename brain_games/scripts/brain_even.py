#!/usr/bin/env python3.


import prompt
from random import randint
from brain_games import cli


def is_even():
    name = ''
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        print('Question: ' + str(random_number))
        user_answer = prompt.string('Your Answer: ')
        correct = ''
        if (random_number%2 == 0 and user_answer == 'yes') or (random_number%2 != 0 and user_answer == 'no'):
            cli.correct_answer()
            i = i + 1
        elif random_number%2 == 0:
            correct = 'yes'
        elif random_number%2 != 0:
            correct = 'no'
            cli.wrong_answer(user_answer, correct, name)
            return
    cli.congrats(name)
       

        

            
