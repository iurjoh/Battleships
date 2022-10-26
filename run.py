# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# creating a board
from random import randint

computer_board = [[" "]*6 for x in range(6)]
player_board = [[" "]*6 for x in range(6)]

def print_board(board):


# create ships
def create_ships()
    for ship in range(5):
        ship_row, ship_column = randint(0, 6), randint(0, 6)
        while board[ship_row][ship_column] == "X"
            ship_row, ship_column = randint(0, 6), randint(0, 6)

# positioning ships on board
def pos_ships():

# counting how many ships were hit
def hit_ships():