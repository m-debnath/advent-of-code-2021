import os

MODULE     = "day03"
INPUT_FILE = "puzzle.txt"
INPUT_DIR  = "input"

diag_report    = []     # creates a 2d array from input
with open(os.path.join(os.getcwd(), INPUT_DIR + "/" + MODULE, INPUT_FILE), "r") as f:
    for line in f:
        diag_report.append([char for char in line[:-1]])

o2_rating = diag_report.copy()
o2_cols = len(o2_rating[0])
for j in range(o2_cols):
    o2_rows = len(o2_rating)
    zero_count = 0
    one_count  = 0
    for i in range(o2_rows):
        if o2_rating[i][j] == "0":
            zero_count += 1
        elif o2_rating[i][j] == "1":
            one_count += 1
    if zero_count > one_count:
        # filter and get all rows starting with 0
        o2_rating = [row for row in o2_rating if row[j] == "0"]
    else:
        # filter and get all rows string with 1
        o2_rating = [row for row in o2_rating if row[j] == "1"]
    if len(o2_rating) == 1:
        break


co2_rating = diag_report.copy()
co2_cols = len(co2_rating[0])
for j in range(co2_cols):
    co2_rows = len(co2_rating)
    zero_count = 0
    one_count  = 0
    for i in range(co2_rows):
        if co2_rating[i][j] == "0":
            zero_count += 1
        elif co2_rating[i][j] == "1":
            one_count += 1
    if zero_count <= one_count:
        # filter and get all rows starting with 0
        co2_rating = [row for row in co2_rating if row[j] == "0"]
    else:
        # filter and get all rows string with 1
        co2_rating = [row for row in co2_rating if row[j] == "1"]
    if len(co2_rating) == 1:
        break

# Converts the binary strings into decimal using int(n, 2)
print(int("".join(o2_rating[0]), 2) * int("".join(co2_rating[0]), 2))
