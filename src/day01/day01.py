import os

MODULE     ="day01"
INPUT_FILE ="puzzle.txt"
INPUT_DIR  ="input"

depth_list  = []
depth_index = 0

with open(os.path.join(os.getcwd(), INPUT_DIR + "/" + MODULE, INPUT_FILE), "r") as f:
    for line in f:
        depth_list.append(int(line))


for index, depth in enumerate(depth_list):
    if index > 0:
        if depth > depth_list[index - 1]:
            depth_index += 1

print(depth_index)