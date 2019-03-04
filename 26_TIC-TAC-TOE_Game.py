'''
Tic Tac Toe Game
  '''

def draw_board(board):
	'''
	Draws a game board
	'''
	print("\n     A   B   C  ")
	for i in range(3):
		print("   "+" ---"*3)
		print(f" {i+1} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
	print("   "+" ---"*3 +"\n")   

def make_move(board,player):
	'''
	Asks user for the move and updates the list
	'''
	move='00'
	while ((move[0] not in '123') or (move[1] not in 'ABC')):
		move = input(f"Your move {player} ({play[player]})! Choose the field (e.g.\"1B\"): ").upper()

	row_names = {'1':0,'2':1,'3':2}
	col_names = {'A':0,'B':1,'C':2}

	row_ind = row_names[move[0]]
	col_ind = col_names[move[1]]

	if board[row_ind][col_ind]==' ':
		board[row_ind][col_ind]=play[player]

def game_over(board, player):
	'''
	Checks if the player won
	rtype: boolean
	'''
	# Success in row
	if any(all(True if board[j][i]==play[player] else False for i in range(3)) for j in range(3)):
		return True
	# Success in column
	elif any(all(True if board[i][j]==play[player] else False for i in range(3)) for j in range(3)):
		return True	
	# Success in diagonal
	elif any([
		all(True if board[i][i]==play[player] else False for i in range(3)),
		all(True if board[i][2-i]==play[player] else False for i in range(3))
		]):
		return True
	return False

# GAME
print("\n >>> Welcome in TIC TAC TOE GAME <<<< \n")

game = [[' ' for j in range(3)] for i in range(3)]
draw_board(game)

player = 'Player1'
play = {'Player1':'x', 'Player2':'o'}

while True:
	make_move(game,player)
	draw_board(game)
	if game_over(game,player):
		break
	# switch the players
	if player == 'Player1':
		player='Player2'
	else:
		player='Player1'

print(">>>> GAME OVER <<<<")
print(f"Congratulations {player}! You WON!!\n")




