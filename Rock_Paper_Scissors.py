player1 = input()
player2 = input()

if player1 == player2:
    print("Tie")
elif player1 == "rock" and player2 == "scissors":
    print("Player 1 wins")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 wins")
elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins")
elif player1 == "paper" and player2 == "scissors":
    print("Player 2 wins")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins")  
