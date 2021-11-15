#!/usr/bin/env python3.

from random import randint
import prompt
from brain_games import cli


ROUNDS = 3


def engine(game_logic):
    name = cli.name
    win_count = 0
    while win_count < ROUNDS:
        correct, question = game_logic()
        game_logic()
        print(question)
        user_answer = prompt.string('Your Answer: ')
        if user_answer == str(correct):
            cli.correct_answer()
            win_count = win_count + 1
        else:
            cli.wrong_answer(user_answer, correct, name)
            return
    cli.congrats(name)


def random_num():
    return randint(1, 100)
