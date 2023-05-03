#!/usr/bin/env python

import random

def check_winner(score_1: int, score_2: int):
    while score_1 == score_2:
        print("Both players have the same score. dices will be thrown untill one player is declared to be the winner.")
        player_1_roll = random.randint(1,6)
        player_2_roll = random.randint(1,6)
        score_1 += player_1_roll
        score_2 += player_2_roll

        print(f"player 1 rolled {player_1_roll} making the new total {score_1}")
        print(f"player 2 rolled {player_2_roll} making the new total {score_2}")

    winning_player, winner_score = ("player 1", score_1) if score_1 > score_2 else ("player 2", score_2)

    print(f"player {winning_player} has won with {winner_score}")
