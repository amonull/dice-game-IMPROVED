from main import roll

game_code = int(input("Enter game code:\n"))

if game_code==123:
    
    player1 = input("Enter in player 1 name:\n")
    player2 = input("Enter in player 2 name:\n")


    print(f"\n{player1} will roll now\n")
    player1_rolls = roll(player1, 0, 0)
    player1_rolls.run()

    print(f"\n{player2} will roll now\n")
    player2_rolls = roll(player2, 0, 0)
    player2_rolls.run()
    
    roll.check_winner(player1_rolls.player_score, player2_rolls.player_score, player1, player2)
