# Scenario

# Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

#     the computer (i.e., your program) should play the game using 'X's;
#     the user (e.g., you) should play the game using 'O's;
#     the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
#     all the squares are numbered row by row starting with 1 (see the example session below for reference)
#     the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
#     the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
#     the computer responds with its move and the check is repeated;
#     don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.

# The example session with the program may look as follows:
from random import randrange
import sys

def display_board(board):
	# The function accepts one parameter containing the board's current status
	# and prints it out to the console.
	for row in board:
		print("\n")
		for cols in row:
			print(" | ", cols, end="")
		print("\n")
		print("-------------------")

# updating board status
# @param board list
# @param move tuple
# @param sign string default X for computer turn 
def update_board(board, move, sign = 'X'):
	try:
		# update board status 
		board[move[0]][move[1]] = sign
		return board
	except TypeError:
		print('invaild type found, board should be a list, move should be a tuple')
	except:
		print('something wrong when updating board')


# move conver tto field sig with tuple of (row, col)
def move_to_field(move):
	move -= 1
	# row , col,
	return (move // 3, move % 3)

#check available field user choose 
def is_move_in_available_field(board, move, available_fields):
	field = move_to_field(move)

	return len(available_fields) and field in available_fields


#check move 
def is_valid_move(move):
	return move > 0 and move < 10

def enter_move(board):
	# The function accepts the board's current status, asks the user about their move, 
	# checks the input, and updates the board according to the user's decision.
	available_fields = make_list_of_free_fields(board)
	while True:
		try:
			display_board(board)
			move = int(input("Player, please enter your move: "))

			if(not is_valid_move(move)):
				print("move not in acceptable range 1-9, please try again")
				continue

			move_field = move_to_field(move)
			# check available field 
			if (move_field not in available_fields):
				print("field already been occupied, please try again")
				continue

			# update board 
			board = update_board(board, move_field, 'O')
			# board check
			if (victory_for(board)):
				break;
		
			# compute turn
			move_field = draw_move(board)
			board = update_board(board, move_field)
			# board check
			if (victory_for(board)):
				break;
			# update available fields
			available_fields = make_list_of_free_fields(board)
		except TypeError as e:
			print("a invaild input found, please try again")
		except Exception as e:
			print("something wrong...")


def make_list_of_free_fields(board):
	# The function browses the board and builds a list of all the free squares; 
	# the list consists of tuples, while each tuple is a pair of row and column numbers.
	available_fields = []
	for row in range(len(board)):
		for col in range(len(board[row])):
			current_field = board[row][col]
			if type(current_field) is int:
				available_fields.append((row, col))
	
	return available_fields            

# return with list of tuples
def get_list_of_horizontal(board):
	list = []
	for ir, row in enumerate(board):
		horizon_list = []
		for ic, col in enumerate(row):
			horizon_list.append(board[ir][ic])
		list.append(tuple(horizon_list))
	return list

# return with list of tuples
def get_list_of_vertical(board):
	list = []
	# go though vertical 
	for ic in range(len(board[0])):
		#init vertical list
		vertical_list = []
		for ir, row in enumerate(board):
			vertical_list.append(board[ir][ic])
		list.append(tuple(vertical_list)) 
	return list

def get_list_of_diagonal(board):
	list = []
	list += get_diagonal_from_board_left_corner(board=board)
	#reverse board and get another diagonal
	reversed_board = get_reversed_board(board)
	list += get_diagonal_from_board_left_corner(reversed_board)
	return list

# return with list of tuples
def get_diagonal_from_board_left_corner(board):
	list = []
	diagonal_list = []
	for i, row in enumerate(board):
		diagonal_list.append(board[i][i])
	list.append(tuple(diagonal_list))
	return list

# reverse the board 
def get_reversed_board(board):
	reversed_board = []
	for row in board:
		# copy row to prevent board got modified
		tmp = row[:]
		tmp.reverse()
		reversed_board.append(tmp)
	return reversed_board

def victory_for(board):
	# The function analyzes the board's status in order to check if 
	# the player using 'O's or 'X's has won the game
	horizontal_list = get_list_of_horizontal(board)
	vertical_list =	get_list_of_vertical(board)
	diagonal_list = get_list_of_diagonal(board)

	all_list = horizontal_list + vertical_list + diagonal_list

	winner_sign = None
	for list in all_list:
		if list[0] == list [1] == list [2]:
			#we have a winner
			winner_sign = list[0]
	
	if (type(winner_sign) is str): 
		display_board(board)
		if (winner_sign == 'O'):
			print ("game over, victory is player ",  winner_sign)
		else:
			print ("game over, victory is computer ", winner_sign)

		return True
	return False

def draw_move(board):
	# The function draws the computer's move and updates the board.
	available_fields = make_list_of_free_fields(board)
	random_field = randrange(len(available_fields))
	return available_fields[random_field]

board = [
	[1, 2, 3],
	[4, "X", 6],
	[7, 8, 9]
]

enter_move(board)