import os

MODULE     = "day02"
INPUT_FILE = "puzzle.txt"
INPUT_DIR  = "input"

pos_x = 0   # starting horizontal position
pos_y = 0   # starting depth
aim   = 0

command_list = []

with open(os.path.join(os.getcwd(), INPUT_DIR + "/" + MODULE, INPUT_FILE), "r") as f:
    for line in f:
        command_list.append(line.split())

for _, command in enumerate(command_list):
    direction = command[0]
    unit = int(command[1])
    if direction == "forward":
        pos_x += unit
        pos_y += aim * unit
    elif direction == "down":
        aim += unit
    elif direction == "up":
        aim -= unit

print(pos_x * pos_y)