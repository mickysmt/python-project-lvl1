#!/usr/bin/env python3.

from brain_games.cli import welcome_user, calc_question
from brain_games.games.brain_calc import game


def main():
    welcome_user()
    calc_question()
    game()


if __name__ == '__main__':
    main()
