def find_ascending(series):
    idx = [(series[0] < series[1]), (series[1] < series[2]), (series[2] < series[3])]
    if idx.count(False) < idx.count(True):
        return False
    else:
        return True


with open("input.txt", "r") as buff:
    safe_asc = [1, 2, 3]
    safe_des = [-1, -2, -3]
    data = buff.readlines()
    counter = 0
    for line in data:
        items = line.split(" ")
        line_safe = True
        ascending = find_ascending(items)
        dampener = 0
        skip = False
        for i in range(len(items) - 1):
            diff = int(items[i]) - int(items[i + 1])
            if skip:
                skip = False
                continue
            elif ascending and diff in safe_asc:
                continue
            elif not ascending and diff in safe_des:
                continue
            elif dampener == 0:
                if diff == 0 or diff in safe_asc or diff in safe_des:
                    dampener = 1
                    # skip = True
                else:
                    line_safe = False
                    print(items)
                    break
            else:
                line_safe = False
                print(items)
                break
        if line_safe:
            counter += 1
    print(counter)
