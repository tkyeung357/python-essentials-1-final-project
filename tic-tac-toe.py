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

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        for cols in row:
            print(cols)

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
def move_to_field_sign(move):
    row = move // 3
    col = move % 3
    return (row, col)

#check available field user choose 
def is_move_in_available_field(board, move, available_fields):
    is_available = False
    field_sign = move_to_field_sign(move)

    if (len(available_fields) > 0):
        for field in available_fields:
            if field_sign == field:
                is_available = True

    return is_available


#check move 
def is_valid_move(move):
    return move > 0 and move < 9

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    available_fields = make_list_of_free_fields(board)
    while True:
        try:
            move = int(input("Player, please enter your move: "))

            if(not is_valid_move(move)):
                print("move not in acceptable range 1-9, please try again")
                continue

            # check available field 
            if (not is_move_in_available_field(board, move, available_fields)):
                print("field already been occupied, please try again")
                continue

            # update board 
            board = update_board(board, move_to_field_sign(move), 'O')
            # check victory
            # compute turn
            draw_move(board)
            # check victory
            # update available fields
            available_fields = make_list_of_free_fields(board)
        except TypeError:
            print("a invaild input found, please try again")
        except:
            print("something wrong...")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    available_fields = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            current_field = board[row][col]
            if type(current_field) is int:
                available_fields.append(current_field)
    
    return available_fields            


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass


def draw_move(board):
    # The function draws the computer's move and updates the board.
    available_fields = make_list_of_free_fields(board)
    random_field = randrange(len(available_fields))
    return update_board(board, available_fields[random_field])

