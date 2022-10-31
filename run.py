# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# from random import randint

# board = []

# for x in range (0, 5):
#     board.append(["0"] * 5)
    
# def print_board(board):
#     for row in board:
#         print(" ".join(row))
        
# def random_row(board):
#     return randint(0, len(board) - 1)

# def random_col(board):
#     return randint(0, len(board[0]) - 1)
    
# ship_row = random_row(board)
# ship_col = random_col(board)

# guess_row = int(input ("Guess row: "))
# guess_col = int(input ("Guess column: "))

# print(ship_row)
# print(ship_col)
# print(board)


from random import randint
size_board = 6
ships = 4
shots = 10
board = []


def instructions():
    """
    starting with some instructions
    """
print("----------------------------------------------")
print("         Welcome to BATTLESHIPS GAME!         ")
print("Board size: 5x5. Number of ships: 4. Shots: 10")
print("----------------------------------------------")
instructions()


def user_name():
    """
    Creating a user name
    """
    user_name_string = input ("Please Commander, enter your name here: ")
    print(f"Welcome Commander {user_name_string},")
    print("We have spoted the battlefield. Enemy ships are hidden.")
    print("You have only 10 chances to sink all 4 enemies.")
    print("Attack with intelligence and precision.")
    print(f"We count on you Commander {user_name_string} to win this war! \n")

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
    print_board(board)


def random_row(board):
    """
    Randomly placing a ship in a row
    """
    return randint(0, 5)

def random_col(board):
    """
    Randomly placing a ship in a column
    """
    return randint(0, 5)
    
ship_row = random_row(board)
ship_col = random_col(board)


print("Commander, where should we aim our artillery?")
"""
Input for the user's guess
"""
guess_row = int(input ("Choose a row:"))
guess_col = int(input ("Choose a column:"))


print(ship_row)
print(ship_col)


#  - message error:
#     if is not a word or valid number
#     if is repeating previous coordinates 
#     if
# # def hit_ships():

# # print users guess

# # print if was a hit or not

# # print how many ships still could be hit

# # repeat the loop of guess

# # end game message
# # win or loss conditions

# # restart button

# # additional features
# - Play against computer
# - Score board