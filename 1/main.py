#
# with open("input.txt") as file:
#     lines =  file.readlines()
#
# instructions = []
# print(lines)
# for line in lines:
#     line = line.strip()
#     factor = 1 if line[0] == "R" else -1
#     amount = int(line[1:])
#     instructions.append(factor*amount)
#
#
# dial = 50
# count = 0
# for instr in instructions:
#     dial = (dial + instr + 100) % 100
#     if dial == 0:
#         count += 1
#
#
#
# print(count)



with open("input.txt") as file:
    lines =  file.readlines()

instructions = []
for line in lines:
    line = line.strip()
    factor = 1 if line[0] == "R" else -1
    amount = int(line[1:])
    instructions.append(factor*amount)


dial = 50
count = 0
print(instructions)
for instr in instructions:
    # positive: int division, negative check whether abs of negative el is larger than dial if so int division
    print(f"dial: {dial}, count: {count}, instruction: {instr}")
    if instr == 0:
        continue
    if instr > 0:
        count += (dial + instr) // 100
    else:
        count += max(0,abs(dial + instr) // 100 + int(dial != 0 and dial <= abs(instr)))
    dial = (dial + instr) % 100

print(count)

