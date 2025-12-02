
# with open("input.txt") as f:
#     content = f.read().strip().split(",")
#     print(content)
#     ranges = [[int(line.split("-")[0]),int(line.split("-")[1])] for line in content]
#     print(ranges)
#
#     sum = 0
#
#     for seq in ranges:
#         for num in range(seq[0], seq[1]+1):
#             #check for doubles
#             #is double when num // 10**(size/2)
#             string = str(num)
#             length = len(string)
#             if length % 2 != 0:
#                 continue
#             if string[:length//2] == string[length//2:]:
#                 sum += num
#
#     print(sum)
#
with open("input.txt") as f:
    content = f.read().strip().split(",")
    print(content)
    ranges = [[int(line.split("-")[0]),int(line.split("-")[1])] for line in content]
    print(ranges)

    sum = 0

    for seq in ranges:
        print(f"range {seq[0]} - {seq[1]}")
        for num in range(seq[0], seq[1]+1):
            #check for doubles
            #is double when num // 10**(size/2)
            string = str(num)
            length = len(string)
            for subsize in range(1,length//2+1):
                if length % subsize != 0:
                    continue
                chunks = []
                for chunk in range(0,length,subsize):
                    chunks.append(str(num)[chunk:chunk+subsize])
                store = True
                for i in range(len(chunks)-1):
                    if chunks[i] != chunks[i+1]:
                        store = False
                if store:
                    print(f"found for num {num} with subsize: {subsize}")
                    sum += num
                    break

    print(sum)

