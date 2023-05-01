# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
from random import randint


def print_board(board):
    """
    Creates a 2d board of the game
    """
    print("   ", end="")
    for col in range(len(board)):
        print(col, end=" ")
    print()

    for row in range(len(board)):
        print(row, end="  ")
        for col in range(len(board[row])):
            print(board[row][col], end=" ")
        print()


def setup_board(size):
    """
    Initializes a game board of a given size.
    """
    board = []
    for _ in range(size):
        board.append(["-"] * size)
    return board


def place_chest(board):
    """
    Randomly places the chest in the game board.
    """
    chest_row = randint(0, len(board) - 1)
    chest_col = randint(0, len(board) - 1)
    return chest_row, chest_col


def get_valid_board_size():
    """
    Asks the player for a valid board size.
    """
    while True:
        size_str = input("Enter the board size (3, 5, or 9): ")
        if size_str.isdigit():
            size = int(size_str)
            if size in [3, 5, 9]:
                return size
        print("Invalid board size. Please enter a valid board size (3, 5, or 9).")


def reveal_chest_location(board, chest_row, chest_col):
    """
    Reveals the location of the chest on the board.
    """
    board[chest_row][chest_col] = "T"


def play_game(name, size):
    """
    Runs the treasure hunt game of a given size.
    """
    board = setup_board(size)
    chest_row, chest_col = place_chest(board)

    # print chest location for testing purposes
    """
    Used in test phase. Must be commented when deploy.
    """
    print(f"Chest located at ({chest_row}, {chest_col})")

    max_guesses = int(size * 1.5)

    print(
        f"Board size: {size}x{size}."
        f" Treasure: 1. Guesses: {max_guesses}.")

    for guess_num in range(1, max_guesses + 1):
        print(
            f"Explorer {name}, where should we dig now?"
            f" Guess {guess_num} of {max_guesses}.")
        print_board(board)

        valid_input = False
        while not valid_input:
            guess_row_str = input("Choose a row: ")
            guess_col_str = input("Choose a column: ")

            if not guess_row_str.isdigit() or not guess_col_str.isdigit():
                print(
                    f"Invalid option, explorer {name}."
                    f" Please, enter valid numbers between 0 and {size - 1}.")
                continue

            guess_row = int(guess_row_str)
            guess_col = int(guess_col_str)

            if guess_row not in range(size) or guess_col not in range(size):
                print(f"Sorry explorer {name}, those coordinates are outside the map.")
                continue

            if board[guess_row][guess_col] == "X":
                print(
                    f"This location was explored."
                    f" Please, try a new one explorer {name}.")
                continue

            valid_input = True

        if guess_row == chest_row and guess_col == chest_col:
            # mark treasure location on board
            board[guess_row][guess_col] = "T"
            print_board(board)
            print("""                ______
             .-'      `-.
           .'            `.
          /                \.
         ;                 ;`
         |          /      |;
         ;         / / /   ;|
         '\       / / /   / ;
          \`.    / /    .' /
           `.`-._____.-' .'
             / /`_____.-'
            / / /
           / / /    
          / / /    "History may be accurate.
         / / /       
        / / /       But archaeology is precise."
       / / /         
      / / /         ― Doug Scott
     / / /
    / / /
    \/_/                          
""")
            print(f"Congratulations explorer {name}! You found the treasure!")
            restart_game(name, size)
            return

        print(f"Sorry, explorer {name}. You missed the treasure!")
        board[guess_row][guess_col] = "X"

    reveal_chest_location(board, chest_row, chest_col)
    print_board(board)
    
    print("""
         ,---,_          ,
          _>   `'-.  .--'/
     .--'` ._      `/   <_
      >,-' ._'.. ..__ . ' '-.       "Failure
   .-'   .'`         `'.     '.
    >   / >`-.     .-'< \ , '._\.    is success
   /    ; '-._>   <_.-' ;  '._>
   `>  ,/  /___\ /___\  \_  /        in progress."
   `.-|(|  \_o/  \_o/   |)|`
       \;        \      ;/           ― Albert Einstein
         \  .-,   )-.  /
          /`  .'-'.  `\.
         ;_.-`.___.'-.;
""")

    print(f"Sorry, explorer {name}. You didn't find the treasure this time.")
    print(f"The treasure was hidden in location ({chest_row}, {chest_col}).")
    restart_game(name, size)


def restart_game(name, size):
    """
    Asks the player if they want to start a new game, and prompts for level choice if they choose to play again.
    """
    valid_input = False
    while not valid_input:
        answer = input(f"Explorer {name}, would you like to start a new Treasure Hunt adventure? (Y/N): ")
        if answer.upper() == "Y":
            print("Please, choose your difficulty level:")
            print("1. Easy (board size: 3x3)")
            print("2. Medium (board size: 5x5)")
            print("3. Hard (board size: 9x9)")
            while True:
                level_choice = input("Enter your choice (1-3): ")
                if level_choice == "1":
                    play_game(name, 3)
                    break
                elif level_choice == "2":
                    play_game(name, 5)
                    break
                elif level_choice == "3":
                    play_game(name, 9)
                    break
                else:
                    print("Invalid choice. Please, enter a number between 1 and 3.")
            valid_input = True
        elif answer.upper() == "N":
            print("Thanks for playing! Come back soon!")
            sys.exit()  # exit the program
        else:
            print("Invalid input. Please, enter Y or N.")


# Start the game

def start_game():
    """
    Starts the Treasure Hunt game.
    """

    print("""******************************************************************
                   |                 |                     |
________________.=\"\";=.______________|_____________________|_____
         |  ,-"_,=\"\"     `\"=.|                  |
_________|__\"=._o`\"-._        `\"=.______________|________________
                `\"=._o`\"=._      _`\"=._                     |
_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|____
         |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |
_________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|________________
           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |
___________| ;`-.o`\"=._; .\" ` '\"`.\` . \"-._ /_______________|____
         | |o;    `\"-.o`\"=._``  '\"` \" ,__.--o;  |
_________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|_________________
/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/__
___/______/_\"=._o--._        ; | ;        ; ;/______/______/______
/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/__
___/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______
/______/______/______/______\"=.o|o_.--\"\"___/______/______/______/_
___/______/______/______/______/______/______/______/______/______
   ).-.o.*)    +-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+    ).-.o.*)
  (:_.:.*(     |T|r|e|a|s|u|r|e| |H|u|n|t| |G|a|m|e|   (:_.:.*(
   )*.-.o.)                                             )*.-.o.)
  (-X_.*:(             |b|y| |i|u|r|j|o|h|             (-X_.*:(
   )-.--.*)    +-+-+-+ +-+-+ +-+-+-+-+-+-+ +-+-+-+-+    )-.--.*)                          
""")

    while True:
        name = input("Welcome explorer! Please, enter your name (only letters): ")
        if name.isalpha() and not name.isdigit():
            # Valid name, proceed with the game
            break
        else:
            # Invalid name, ask again
            print("Invalid name. Please, enter a non-empty name with only letters from A to Z.")

    while True:
        print("Please, choose your difficulty level:")
        print("1. Easy (board size: 3x3)")
        print("2. Medium (board size: 5x5)")
        print("3. Hard (board size: 9x9)")

        level_choice = input("Enter your choice (1-3): ")
        if level_choice == "1":
            play_game(name, 3)
            restart_game(name, 3)
            break
        elif level_choice == "2":
            play_game(name, 5)
            restart_game(name, 5)
            break
        elif level_choice == "3":
            play_game(name, 9)
            restart_game(name, 9)
            break
        else:
            print("Invalid choice. Please, enter a number between 1 and 3.")

start_game()
