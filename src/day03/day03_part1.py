import os

MODULE     = "day03"
INPUT_FILE = "puzzle.txt"
INPUT_DIR  = "input"

diag_rows      = 0
diag_cols      = 0
diag_report    = []     # creates a 2d array from input

gamma_digits   = []     # 5 digit binary number
epsilon_digits = []     # 5 digit binary number

with open(os.path.join(os.getcwd(), INPUT_DIR + "/" + MODULE, INPUT_FILE), "r") as f:
    for line in f:
        diag_report.append([char for char in line[:-1]])

diag_rows = len(diag_report)
diag_cols = len(diag_report[0])

for j in range(diag_cols):
    zero_count = 0
    one_count  = 0
    for i in range(diag_rows):
        if diag_report[i][j] == "0":
            zero_count += 1
        elif diag_report[i][j] == "1":
            one_count += 1
    if zero_count > one_count:
        gamma_digits.append("0")
        epsilon_digits.append("1")
    else:
        gamma_digits.append("1")
        epsilon_digits.append("0")

# Converts the binary strings into decimal using int(n, 2)
print(int("".join(gamma_digits), 2) * int("".join(epsilon_digits), 2))
