# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from random import randint

board = []


def instructions():
    """
    starting with some instructions
    """
print("----------------------------------------------")
print("         Welcome to BATTLESHIPS GAME!         ")
print("Board size: 6x6. Number of ships: 4. Shots: 10")
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
    for row in range(6):
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

# used to test the game during coding
print(ship_row)
print(ship_col)

shots = 0

while shots < 10:
    print("Commander, where should we aim our artillery?")
    """
    Input for the user's guess
    """
    guess_row = int(input ("Choose a row:"))
    guess_col = int(input ("Choose a column:"))


    # If the target was hit
    if guess_row == ship_row and guess_col == ship_col:
        print("Bull's-eye Commander! You sank one ship!")
        # After 10 shots
        break

    # If the shoot are outside the battlefield
    elif guess_row not in range(6) or guess_col not in range(6):
        print("Sorry Commander, these coordinates are outside the battlefield.")

    # If was already choosen
    elif board[guess_row][guess_col] == "X":
        print("Commander, This coordinate has already been assigned.")


    # If you missed the target
    else:
        print("Commander you missed the target")
        board[guess_row][guess_col] = "X"
        print_board(board)
        # Removing a user's chance
        shots += 1
    


# print how many ships still could be hit

# end game message
# win or loss conditions

# restart button

# additional features
# - Play against computer
# - Score board