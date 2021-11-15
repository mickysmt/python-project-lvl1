#!/usr/bin/env python3.

from brain_games.cli import welcome_user, is_prime_rule
from brain_games.games.brain_is_prime import game


def main():
    welcome_user()
    is_prime_rule()
    game()


if __name__ == '__main__':
    main()
