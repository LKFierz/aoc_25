# import numpy as np
#
# with open("input.txt") as f:
#     lines = f.readlines()
# stripped_lines = [line.strip() for line in lines]
# numbers_strings = stripped_lines[:-1]
# operators_strings = stripped_lines[-1]
#
# print(numbers_strings)
#
# numbers = np.array([[num for num in line.split(" ") if num != ""]for line in numbers_strings],dtype=int)
#
# operators = np.array([op for op in operators_strings.split(" ") if op != ""])
#
# count = 0
# print(numbers.shape)
#
# for col in range(numbers.shape[1]):
#     op = operators[col]
#     if op == "+":
#         count += np.sum(numbers[:,col])
#     elif op == "*":
#         count += np.prod(numbers[:,col])
#
#
# print(count)
#
#
#
import numpy as np

with open("test.txt") as f:
    lines = f.readlines()
stripped_lines = [line.strip() for line in lines]
print(stripped_lines)
numbers_strings = np.array([[char for char in line] for line in stripped_lines[:-1]])
operators_strings = stripped_lines[-1]

operators = np.array([op for op in operators_strings.split(" ") if op != ""])
# print(f"operators: {operators}")
# print(f"numbers: {numbers_strings}")

count = 0
op_id = 0
numbers = []

for col_id in range(len(numbers_strings[0])):
    column = numbers_strings[:,col_id]
    if np.all(column == " "):
        if operators[op_id] == "+":
            count += np.sum(numbers)
        elif operators[op_id] == "*":
            count += np.prod(numbers)
        numbers = []
        op_id += 1
        continue
    number = int("".join([entry for entry in column if entry != " "]))
    numbers.append(number)

     


print(count)

    

