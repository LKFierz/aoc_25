# with open("input.txt") as f:
#     lines = f.readlines()
#     stripped_lines = [line.strip() for line in lines]
#     sum = 0
#
#
#
#     for line in stripped_lines:
#         if len(line) == 0:
#             continue
#         if len(line) == 1:
#             sum += int(line[0])
#             continue
#         max_index = 0
#         max = int(line[0]) 
#         for i in range(1, len(line)-1):
#             num = int(line[i])
#             if num > max:
#                 max = num
#                 max_index = i
#         second_max = int(line[max_index+1])
#         for j in range(max_index + 2 , len(line)):
#             num = int(line[j])
#             if num > second_max:
#                 second_max = num
#         sum += max*10 + second_max
#
#     print(sum)
#
#
#
#
with open("input.txt") as f:
    lines = f.readlines()
    stripped_lines = [line.strip() for line in lines]
    sum = 0

    
    
    for line in stripped_lines:
        if len(line) == 0:
            continue
        if len(line) < 12:
            sum += int(line)
            continue
        max_index = -1 
        first_max = -1
        for i in range(len(line)-11):
            num = int(line[i])
            if num > first_max or num == 1 and first_max == 1:
                first_max = num
                max_index = i
        joltage = first_max
        print(f"first_index {max_index} and value {first_max}")
        for i in range(10,-1,-1):
            max = -1 
            for i in range(max_index + 1, len(line)-i):
                num = int(line[i])
                if num > max or num == 1 and max == 1:
                    max = num
                    max_index = i
            print(f"increasing joltage using index {max_index} and value {max}")
            joltage *= 10
            joltage += max
        print(f"increasing by {joltage}")
        sum += joltage

    print(sum)

        


