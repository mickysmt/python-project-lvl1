#!/usr/bin/env python3.

from brain_games.games.game_engine import engine, random_num


def game_logic():
    random_number = random_num()
    question = ('Question: ' + str(random_number))
    return ('no' if random_number % 2 else 'yes', question)


def game():
    engine(game_logic)
