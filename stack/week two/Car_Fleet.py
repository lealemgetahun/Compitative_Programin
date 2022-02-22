def carFleet(target, position, speed):
    dic_speed ={}
    dic_sum = {}
    stack = []
    # for i in position:
    #     dic[i] = i
    for i in range(len(position)):
        dic_speed[position[i]] = speed[i]
        dic_sum[position[i]] = position[i] + speed[i]

#         sort = dict(sorted(dic_speed.items(), key=lambda item: item[1]))
    
    sort = sorted(dic_speed)
    sort = sort[::-1]
    # print(sort)
    for pos in sort:
        speed = dic_speed[pos]
        dist = target - pos
        t = dist/speed
        if not stack:
            stack.append(t)
        elif t > stack[-1]:
            stack.append(t)
    print(stack)
    return len(stack)