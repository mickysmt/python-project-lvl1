#!/usr/bin/env python3.

from brain_games.game_engine import run
from brain_games.games import brain_is_prime


def main():
    run(brain_is_prime)


if __name__ == '__main__':
    main()
