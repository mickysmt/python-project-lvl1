#!/usr/bin/env python3.


import prompt
from random import randint


def parity_of_numbers():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        print('Question: ' + str(random_number))
        your_answer = prompt.string('Your answer: ')

        if random_number%2 == 0 and your_answer == 'yes':
            i = i + 1
            print('Correct!')
        elif random_number%2 != 0 and your_answer == 'no':
            i = i + 1
            print('Correct!')
        elif random_number%2 == 0 and your_answer == 'no':
            print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.\nLet\'s try again, ' + name + '!')
            return
        elif random_number%2 != 0 and your_answer == 'yes':
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.\nLet\'s try again, ' + name + '!')
            return
        elif random_number%2 != 0 or your_answer != 'no':
            print('\'' + your_answer + '\' is wrong answer ;(. Correct answer was \'no\'.\nLet\'s try again, ' + name + '!')
            return
        elif random_number%2 == 0 and your_answer != 'yes' :
            print('\'' + your_answer + '\' is wrong answer ;(. Correct answer was \'yes\'.\nLet\'s try again, ' + name + '!')
            return
    
    return print('Congratulations, ' + name + '!')
