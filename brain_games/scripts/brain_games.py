#!/usr/bin/env python3.

from brain_games.cli import intro, welcome_user
from brain_games.games.brain_even import is_even


def main():
    welcome_user()
    intro()
    is_even()


if __name__ == '__main__':
    main()
