#!/usr/bin/env python3.

from brain_games.cli import intro, welcome_user, calc_question, gcd_question
from brain_games.games.brain_calc import calc
from brain_games.games.brain_gcd import gcd_func
from brain_games.games.brain_even import is_even


def main():
    welcome_user()
    intro()
    is_even()
    calc_question()
    calc()
    gcd_question()
    gcd_func()


if __name__ == '__main__':
    main()
