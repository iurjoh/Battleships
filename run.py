# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from random import randint
size_board = 6


def instructions():
    """
    starting with some instructions
    """
print("----------------------------------------------")
print("         Welcome to BATTLESHIPS GAME!         ")
print("Board size: 5x5. Number of ships: 4. Shots: 10")
print("----------------------------------------------")
instructions()


# creating a user name
def user_name():
    """
    Creating a user name
    """
    user_name_string = input ("Please Commander, enter your name here: ")
    print(f"Welcome Commander {user_name_string},")
    print("We have spoted the battlefield. Enemy ships are hidden.")
    print("You have only 10 chances to sink all 4 enemies.")
    print("Attack with intelligence and precision.")
    print(f"We count on you Commander {user_name_string} to win this war!")
user_name()


def print_board(board):
    """
    Creating a 2d board to the game
    """
    print("    0 1 2 3 4 5 ")
    print("  +-------------+")
    for row in range(6):
        board.append(["-"] * 6)
    letter = 0
    for row in range(5):
        print(chr(letter + 65), end= " | ")
        # 65 for letter "A" and "end =" makes line one in the top of the other
        for column in range(len(board[letter])):
            print(board[letter][column], end= " ")
        print("| ")
        letter += 1
    print("  +-------------+")

board = []

print_board(board)

# # create ships
# def create_ships()
#     """
#     Creating ships on the board suing a random position
#     """
#     for ship in range(5):
#         ship_row, ship_column = randint(0, 6), randint(0, 6)
#         while board[ship_row][ship_column] == "X":
#             ship_row, ship_column = randint(0, 6), randint(0, 6)
#         board[ship_row][ship_column] = "X"


# # positioning ships on board
# def pos_ships():

# # counting how many ships were hit
# def hit_ships():