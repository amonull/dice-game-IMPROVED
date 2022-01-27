import random
import time

class roll:
    def __init__(self, player_name, player_total, player_score):
        self.player_name = player_name
        self.player_total = player_total
        self.player_score = player_score

    def run(self):
        for x in range (5):

            first_roll = random.randint(1,6)
            second_roll = random.randint(1,6)
            self.player_total = first_roll+second_roll
            print(f"you rolled {first_roll} and {second_roll} making your total {self.player_total}")

            if first_roll == second_roll:
                print("duplicate roll rolling another dice")
                duplicate_roll = random.randint(1,6)
                self.player_total =+ duplicate_roll
                print(f"you rolled {duplicate_roll}")
                time.sleep(1)

            if self.player_total%2 == 0:
                    print("your number is even you get +10 points")
                    self.player_score = (self.player_score + 10)
                    print(f"{self.player_name} score is {self.player_score}\n")
                    time.sleep(1)

            else:
                print("your number is odd you get -5 points")
                self.player_score = (self.player_score - 5)
                print(f"{self.player_name} score is {self.player_score}\n")
                if self.player_score < 0:
                    self.player_score = self.player_score*0
                    print(f"{self.player_name} score is {self.player_score}\n")
                    time.sleep(1)

    @classmethod
    def check_winner(self, player1, player2, player_name1, player_name2):
        self.player1 = player1
        self.player2 = player2
        self.player_name1 = player_name1
        self.player_name2 = player_name2

        while player1 == player2:
            print("both players have the same score dice will be thrown untill one player is declared the winner.")
            draw_roll1 = random.randint(1,6)
            draw_roll2 = random.randint(1,6)
            self.player1 = (self.player1 + draw_roll1)
            self.player2 = (self.player2 + draw_roll2)
            print(f"{self.player_name1} has rolled {draw_roll1}")
            print(f"{self.player_name2} has rolled {draw_roll2}")
        if player1 > player2:
            print(f"{self.player_name1} has won! with {self.player1} points")
        elif player1 < player2:
            print(f"{self.player_name2} has won! with {self.player2} points")
