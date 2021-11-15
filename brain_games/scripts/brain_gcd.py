#!/usr/bin/env python3.

from brain_games.cli import welcome_user, gcd_question
from brain_games.games.brain_gcd import game


def main():
    welcome_user()
    gcd_question()
    game()


if __name__ == '__main__':
    main()
