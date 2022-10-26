# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from random import randint

"""
    starting the game and giving instructions
"""
print("___________________________________")
print("Welcome to BATTLESHIPS GAME!")
print("Board size: 5. Number of ships: 4.")
print("___________________________________")

# creating a board
computer_board = [[" "]*6 for x in range(6)]
player_board = [[" "]*6 for x in range(6)]

def print_board(board):


# create ships
def create_ships()
    """
    Creating ships on the board suing a random position
    """

    for ship in range(5):
        ship_row, ship_column = randint(0, 6), randint(0, 6)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 6), randint(0, 6)
        board[ship_row][ship_column] = "X"


# positioning ships on board
def pos_ships():

# counting how many ships were hit
def hit_ships():