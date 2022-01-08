import os
from copy import deepcopy
from pprint import pprint

MODULE     = "day04"
INPUT_FILE = "puzzle.txt"
INPUT_DIR  = "input"

numbers_to_draw = []
bingo_boards    = []
bingo_marked    = []
board_rows      = 5
board_cols      = 5
winning_list    = [True] * 5
winning_number  = -1
winning_sum     = 0

# reads file input and creates list of numbers to draw and list of bingo boards
with open(os.path.join(os.getcwd(), INPUT_DIR + "/" + MODULE, INPUT_FILE), "r") as f:
    numbers_to_draw = f.readline()[:-1].split(",")
    board = []
    insert_rows = 0
    for line in f:
        if not line.startswith("\n"):
            board.append([digit for digit in line[:-1].split(" ") if digit != ""])
            insert_rows += 1
            if insert_rows == board_rows:
                bingo_boards.append(board)
                insert_rows = 0
                board = []

# creates a copy of list of bingo boards to be used for marking
bingo_marked = deepcopy(bingo_boards)
for i, board in enumerate(bingo_marked):
    for j, row in enumerate(board):
        for k, _ in enumerate(row):
            bingo_marked[i][j][k] = False

# number draw starting
for number in numbers_to_draw:
    for i, board in enumerate(bingo_boards):
        for j, row in enumerate(board):
            for k, _ in enumerate(row):
                if bingo_boards[i][j][k] == number:
                    bingo_marked[i][j][k] = True
    for i, board in enumerate(bingo_marked):
        for j, row in enumerate(board):
            if row == winning_list:
                winning_number = int(number)
                winning_index = i
                break
        else:
            invert_board = [list(x) for x  in zip(*board)]
            for j, row in enumerate(invert_board):
                if row == winning_list:
                    winning_number = int(number)
                    winning_index = i
                    break
            else:
                continue
        break
    else:
        continue
    break

for i, row in enumerate(bingo_boards[winning_index]):
    for j, digit in enumerate(row):
        if not bingo_marked[winning_index][i][j]:
            winning_sum += int(digit)

print(winning_sum * winning_number)
