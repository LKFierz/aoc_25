
# with open("input.txt") as f:
#     content = f.read()
#     string_ranges = content.split("\n\n")[0]
#     string_ids = content.split("\n\n")[1]
#
#     ranges = [[int(line.split("-")[0]), int(line.split("-")[1])] for line in string_ranges.split("\n")]
#     ids = [int(entry) for entry in string_ids.strip().split("\n")]
#
#     count = 0 
#
#     for id in ids:
#         print(f" id: {id}")
#         for range in ranges:
#             if id >= range[0] and id <= range[1]:
#                 count += 1
#                 print("increasing")
#                 break
#
#
#     print(count)

with open("input.txt") as f:
    content = f.read()
    string_ranges = content.split("\n\n")[0]
    string_ids = content.split("\n\n")[1]

    ranges = [[int(line.split("-")[0]), int(line.split("-")[1])] for line in string_ranges.split("\n")]
    print(ranges)
    sorted_ranges = sorted(ranges,key=lambda x: x[0])
    print(sorted_ranges)
    #order ranges


    count = 0 

    filtered_ranges = []
    for seq in sorted_ranges:
        should_add = True
        for existing in filtered_ranges:
            if (existing[0] <= seq[0] and existing[1] >= seq[0]) or (existing[0] <= seq[1] and existing[1] >= seq[1]):
                existing[0] = min(existing[0], seq[0])
                existing[1] = max(existing[1], seq[1])
                should_add = False
                break
        if should_add:
            filtered_ranges.append(seq)


    for existing in filtered_ranges:
        increment = (existing[1] - existing[0]) + 1
        count += increment



    print(count)
