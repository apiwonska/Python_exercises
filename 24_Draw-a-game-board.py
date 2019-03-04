'''
Print a custom sized game board. 
'''

def draw_board(width, height):
	for h in range(height):
		print(' ---'*width +'\n'+'|   '*(width+1))
	print(' ---'*width )

if __name__ == "__main__":
	
	width = int(input("Please specify the width of the board:  "))
	height = int(input("Please specify the height of the board:  "))

	draw_board(width, height)