# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from random import randint

board = []


def instructions():
    """
    starting with some instructions
    """
print("------------------------------------------")
print("         Welcome to TREASURE HUNT!        ")
print("Board size: 5x5. Treasure: 1. Chances: 10.")
print("------------------------------------------")
instructions()


def user_name():
    """
    Creating a user name
    """
    user_name_string = input ("Please explorer, enter your name here: ")
    print(f"Welcome explorer {user_name_string},")
    print("There is a chest full of treasures, but it's hidden around here.")
    print("You have only 10 chances to find your treasure.")
    print("Choose a place to dig with intelligence and precision.")
    print(f"Good luck, explorer {user_name_string}! \n")

user_name()


def print_board(board):
    """
    Creating a 2d board to the game
    """
    print("    0 1 2 3 4  ")
    print("  +-----------+")
    for row in range(5):
        board.append(["-"] * 5)
    number = 0
    for row in range(5):
        print((number), end= " | ")
        for column in range(len(board[number])):
            print(board[number][column], end= " ")
        print("| ")
        number += 1
    print("  +-----------+")
print_board(board)


def random_row(board):
    """
    Randomly placing a chest in a row
    """
    return randint(0, 4)

def random_col(board):
    """
    Randomly placing a chest in a column
    """
    return randint(0, 4)
    
chest_row = random_row(board)
chest_col = random_col(board)

# used to test the game during coding
# print(chest_row)
# print(chest_col)

guesses = 0

while guesses < 10:
    print("Explorer, where should we dig now?")
    """
    Input for the user's guess
    """
    guess_row = int(input ("Choose a row:"))
    guess_col = int(input ("Choose a column:"))


    # If the chest was discovered
    if guess_row == chest_row and guess_col == chest_col:
        print("'History may be accurate. But archaeology is precise.' - Doug Scott")
        print("Congratulations, you finally found the treasure!")

        # After 10 guesses
        break

    # If the shoot are outside the battlefield
    elif guess_row not in range(5) or guess_col not in range(5):
        print("Sorry, these coordinates are outside of the map.")


    # If was already choosen
    elif board[guess_row][guess_col] == "X":
        print("Sorry, this coordinate has already been assigned.")


    # If you missed the target
    else:
        print("Ops, there is no treasure here. Try again.")
        board[guess_row][guess_col] = "X"
        print_board(board)
        
        # Removing a user's chance
        guesses += 1
        print("You already used", guesses, "of 10 guesses.")

        if guesses == 10:
            print("Sorry great explorer, but this time you didn't find the treasure!")
