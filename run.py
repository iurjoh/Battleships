# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# creating a board
board = []
for x in range(5):
    board.append([" "] * 5)

def print_board(board):
    for row in board:
        print(row)

print_board(board)
