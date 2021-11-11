#!/usr/bin/env python3.

import prompt
from random import randint, choice
from brain_games import cli


def progression():
    name = cli.name
    count = 0
    while count < 3:
        a = randint(1, 100)
        d = randint(1, 20)
        list = [a, a + d, a + 2 * d, a + 3 * d, a + 4 * d]
        for_choice = [0, 1, 2, 3, 4]
        choice_index = choice(for_choice)
        correct = list[choice_index]
        list[choice_index] = '..'
        print('Question: ' + ' '.join([str(i) for i in list]))
        user_answer = prompt.string('Your Answer: ')
        if user_answer == str(correct):
            cli.correct_answer()
            count = count + 1
        else:
            cli.wrong_answer(user_answer, correct, name)
            return
    cli.congrats(name)
