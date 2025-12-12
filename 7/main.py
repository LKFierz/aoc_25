import numpy as np


# with open("input.txt") as f:
#     map = np.array([[entry for entry in list(line.strip())] for line in f.readlines()])
#
# print(f"map\n: {map}")
# start_indx = np.where(map == "S")
# occupied_cols = {start_indx[1][0]}
# count = 0
#
# for row in range(map.shape[0]):
#     new_indexes = set()
#     for col in occupied_cols:
#         #prep position for vertical move
#         if map[row,col] == "^":
#             count += 1
#             new_indexes.add(col-1)
#             new_indexes.add(col+1)
#         else:
#             new_indexes.add(col)
#     occupied_cols = new_indexes
#
#
# print(f"count: {count}")
#
#
#
#
with open("input.txt") as f:
    map = np.array([[entry for entry in list(line.strip())] for line in f.readlines()])

print(f"map\n: {map}")
start_indx = np.where(map == "S")
occupied_cols = np.zeros_like(map[0,:],dtype=int) 
occupied_cols[start_indx[1][0]] = 1
count = 0


for row in range(map.shape[0]):
    new_indexes = np.zeros_like(map[0,:],dtype=int) 
    print(f"occupied before: {occupied_cols}")
    for col, num in enumerate(occupied_cols):
        #prep position for vertical move
        if map[row,col] == "^":
            print("found")
            new_indexes[col-1] += num
            new_indexes[col+1] += num
        else:
            new_indexes[col] += num
    occupied_cols = new_indexes
    print(f"occupied after: {occupied_cols}")

print(f"type of occupied_cells {type(occupied_cols)}")

print(f"count: {np.sum(occupied_cols)}")




