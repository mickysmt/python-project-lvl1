#!/usr/bin/env python3.


from brain_games.games.game_engine import engine, random_num


def is_prime_logic(num):
    i = 2
    if num < 2:
        return False
    elif i >= 2:
        while i <= num / 2:
            if num % i == 0:
                return False
            i += 1
        return True


def game_logic():
    number = random_num()
    question = ('Question: ' + str(number))
    if is_prime_logic(number) is True:
        correct = 'yes'
    else:
        correct = 'no'
    return(correct, question)


def game():
    engine(game_logic)
