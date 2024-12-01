from operator import le


with open("input.tsv", "r") as buff:
    le = []
    ri = []
    for x in buff.readlines():
        temp = x.split("   ")
        le.append(int(temp[0]))
        ri.append(int(temp[1].strip("\n")))
    le.sort()
    ri.sort()
    sum = 0
    for i in range(len(le)):
        sum += abs(le[i] - ri[i])
    print(sum)
