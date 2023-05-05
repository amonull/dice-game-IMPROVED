#!/usr/bin/env python

import random

def roll_for_one_player() -> int:
    player_score = 0

    for _ in range(5):
        first_roll = random.randint(1,6)
        second_roll = random.randint(1,6)
        total = first_roll + second_roll

        print(f"you rolled {first_roll} and {second_roll} making your total {total}")

        if first_roll == second_roll:
            print("first and second rolls are the same rolling third die")
            third_roll = random.randint(1,6)
            total += third_roll

            print(f"you rolled {third_roll} making your new total {total}")

        if not total % 2:
            print("total is even +10 added to score")
            player_score += 10
            print(f"score is {player_score}")
        else:
            print("odd rolled -5 points")
            player_score -= 5
            if player_score < 0:
                player_score *= 0;
            print(f"score is {player_score}")

    return player_score