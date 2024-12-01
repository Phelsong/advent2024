with open("input.tsv", "r") as buff:
    le = []
    ri = []
    for x in buff.readlines():
        temp = x.split("   ")
        le.append(int(temp[0]))
        ri.append(int(temp[1].strip("\n")))
    sum = 0
    for y in le:
        occur = 0
        for i in ri:
            if i == y:
                occur += 1
        sum += y * occur
    print(sum)
