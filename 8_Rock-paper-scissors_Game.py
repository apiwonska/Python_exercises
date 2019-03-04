'''
Rock, paper, scissors game
'''

print("\n >>> Rock, Paper, Scissors <<< \n")

total_p1 = 0
total_p2 = 0

play = 'y'

while play == 'y':

    player1 = input('Player 1, your turn:  ').lower()
    while player1 not in ['paper', 'rock', 'scissors']:
        player1 = input("Please choose 'paper','rock' or 'scissors'  ").lower()

    player2 = input('Player 2, your turn:  ').lower()
    while player2 not in ['paper', 'rock', 'scissors']:
        player2 = input("Please choose 'paper','rock' or 'scissors'  ").lower()

    if player1 == player2:
        print("\nIt's a tie!")
    elif (
        (player1 == 'paper' and player2 == 'rock') or
        (player1 == 'rock' and player2 == 'scissors') or
        (player1 == 'scissors' and player2 == 'paper')
    ):
        print("\nPlayer 1 wins!")
        total_p1 += 1
    else:
        print("\nPlayer 2 wins!")
        total_p2 += 1

    play = input("Do you want to play again? (y/n)  ").lower()

print("\n >>> RESULTS <<< \n")
print("Player 1:", total_p1)
print("Player 2:", total_p2)

if total_p1 > total_p2:
    print("Player 1 wins the game!")
elif total_p1 < total_p2:
    print("Player 2 wins the game!")
else:
    print("It's a tie!")
