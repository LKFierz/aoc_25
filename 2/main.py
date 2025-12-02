
with open("test.txt") as f:
    content = f.read().strip().split(",")
    print(content)
    ranges = [[int(line.split("-")[0]),int(line.split("-")[1])] for line in content]
    print(ranges)

    sum = 0

    for seq in ranges:
        for num in range(seq[0], seq[1]+1):
            #check for doubles
            #is double when num // 10**(size/2)
