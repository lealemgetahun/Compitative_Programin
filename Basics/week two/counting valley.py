
def countingValleys(steps, path):
    sea_level = 0
    count = 0
    for i in range(steps):
        if path[i] == 'U':
            sea_level += 1
        elif path[i] == 'D':
            sea_level -= 1
            if sea_level == -1:
                count += 1
    return count