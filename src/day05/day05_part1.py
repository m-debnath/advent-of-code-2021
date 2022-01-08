import os
from pprint import pprint

MODULE     = "day05"
INPUT_FILE = "puzzle.txt"
INPUT_DIR  = "input"

vent_lines       = []
max_coordinate   = -1
limit_coordinate = -1

# reads file input and creates list of numbers to draw and list of bingo boards
with open(os.path.join(os.getcwd(), INPUT_DIR + "/" + MODULE, INPUT_FILE), "r") as f:
    for line in f:
        line_points = line[:-1].split(" -> ")
        line_coordinates = []
        for point in line_points:
            line_coordinates.append([int(xy) for xy in point.split(",")])
        vent_lines.append(line_coordinates)

# Calculate the maximum coordinate of the plane e.g. 9, 99, 999 etc.
for line in vent_lines:
    for point in line:
        for xy in point:
            if xy > max_coordinate:
                max_coordinate = xy
limit_coordinate = pow(10, len(str(max_coordinate)))

# declare a 2d area with risk 0 at all points
vent_area = []
for i in range(limit_coordinate):
    area_line = []
    for j in range(limit_coordinate):
        area_line.append(0)
    vent_area.append(area_line)

# get only horizonal or vertival or diagonal vent line i.e. for x1,y1 -> x2,y2, x1 = x2 or y1 = y2
vent_horizontal_vertical_lines = []
for line in vent_lines:
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        vent_horizontal_vertical_lines.append(line)

# calculate risks for horizontal and vertical vent lines
for line in vent_horizontal_vertical_lines:
    if line[0][0] == line[1][0]:
        if line[0][1] < line[1][1]:
            for i in range(line[0][1], line[1][1] + 1):
                vent_area[i][line[0][0]] += 1
        else:
            for i in range(line[1][1], line[0][1] + 1):
                vent_area[i][line[0][0]] += 1
    if line[0][1] == line[1][1]:
        if line[0][0] < line[1][0]:
            for i in range(line[0][0], line[1][0] + 1):
                vent_area[line[0][1]][i] += 1
        else:
            for i in range(line[1][0], line[0][0] + 1):
                vent_area[line[0][1]][i] += 1

risk_score = 0
for row in vent_area:
    for col in row:
        if col >= 2:
            risk_score += 1

pprint(risk_score)
