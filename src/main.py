#!/usr/bin/env python

import sys

from utils.rolls import roll_for_one_player
from utils.check_winners import check_winner


def validation():
    attempt_counter = 0
    game_code = 0
    while True:
        if attempt_counter > 10:
            print("too many failed attempts")
            sys.exit(-1)

        try:
            game_code = int(input("Enter game code: "))
            if game_code != 123:
                print("wrong code try again")
                attempt_counter += 1
        except ValueError:
            print("wrong code try again")
            attempt_counter += 1

        if game_code == 123:
            break

def main():
    player_1_rolls = roll_for_one_player()
    player_2_rolls = roll_for_one_player()

    check_winner(player_1_rolls, player_2_rolls)

if __name__ == "__main__":
    validation()
    main()
