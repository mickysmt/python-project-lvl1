#!/usr/bin/env python3.

import prompt
from brain_games.cli import welcome_user

NUMBER_OF_ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    print(game.RULE)
    for win_count in range(NUMBER_OF_ROUNDS):
        correct, question = game.generate_round()
        print(question)
        user_answer = prompt.string('Your Answer: ')
        if user_answer == str(correct):
            print('Correct!')
        else:
            wrong = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(wrong.format(user_answer, correct))
            print("Let's try again, {}!".format(user_name))
            return
    print('Congratulations, {}!'.format(user_name))
