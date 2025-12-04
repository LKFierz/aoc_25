import numpy as np


DIRECTIONS = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def check_around(row: int, col: int, map):
    neighbors = 0
    rows = len(map)
    cols = len(map[0])
    for dir in DIRECTIONS:
        if row + dir[0] < rows and row + dir[0] >= 0 and col + dir[1] < cols and col + dir[1] >= 0:
            neighbors += int(map[row + dir[0]][col + dir[1]] == "@")

    return neighbors

with open("input.txt") as f:
    lines = f.readlines()
    map = [list(line.strip()) for line in lines]
    count = 0
    removed = -1
    while removed != 0:
        removed = 0
        to_be_removed = dict()
        # print(np.array(map))
        for row in range(len(map)):
            for col in range(len(map[0])):
                if map[row][col] == "@" and check_around(row,col,map) < 4:
                    # print(f"adding {row}, {col}")
                    if row in to_be_removed.keys():
                        to_be_removed[row].append(col)
                    else:
                        to_be_removed[row] = [col]
                    count += 1
                    removed += 1
        # print(f"removing {removed} items")
        # print(f"dictionary: {to_be_removed}")
        for row,cols in to_be_removed.items():
            for col in cols:
                map[row][col] = "x"
        


    print(count)



