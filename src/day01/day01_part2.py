import os

MODULE     = "day01"
INPUT_FILE = "puzzle.txt"
INPUT_DIR  = "input"

depth_list  = []
depth_index = 0
sum_degree  = 3

with open(os.path.join(os.getcwd(), INPUT_DIR + "/" + MODULE, INPUT_FILE), "r") as f:
    for line in f:
        depth_list.append(int(line))

for index, _ in enumerate(depth_list):
    sum_prev    = 0
    sum_curr    = 0
    if index > len(depth_list) - sum_degree:
        break
    if index > 0:
        for depth in depth_list[index-1 : index+sum_degree-1]:
            sum_prev += depth
        for depth in depth_list[index : index+sum_degree]:
            sum_curr += depth
        if sum_curr > sum_prev:
            depth_index += 1

print(depth_index)