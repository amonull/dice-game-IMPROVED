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

#     @classmethod
#     def check_winner(self, player1, player2, player_name1, player_name2):
#         self.player1 = player1
#         self.player2 = player2
#         self.player_name1 = player_name1
#         self.player_name2 = player_name2

#         while player1 == player2:
#             print("both players have the same score dice will be thrown untill one player is declared the winner.")
#             draw_roll1 = random.randint(1,6)
#             draw_roll2 = random.randint(1,6)
#             self.player1 = (self.player1 + draw_roll1)
#             self.player2 = (self.player2 + draw_roll2)
#             print(f"{self.player_name1} has rolled {draw_roll1}")
#             print(f"{self.player_name2} has rolled {draw_roll2}")
#         if player1 > player2:
#             print(f"{self.player_name1} has won! with {self.player1} points")
#         elif player1 < player2:
#             print(f"{self.player_name2} has won! with {self.player2} points")
