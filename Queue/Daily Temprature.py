def dailyTemperatures(temperatures):
    dic = {}
    out = []
    stack = []
    stack.append((temperatures[0],0))
    
    for i in range(len(temperatures)):
        # print(stack)
        y = stack[-1][0]
        if y < temperatures[i]:
            while stack and stack[-1][0] <temperatures[i]:
                x = stack.pop()
                dic[x[1]] = i
            stack.append((temperatures[i],i))
        else:
            # x = stack.pop()
            dic[i] = 0
            stack.append((temperatures[i],i))
    while stack:
        x = stack.pop()
        dic[x[1]] = x[1]
        
    for i in sorted(dic):
        out.append(dic[i]-i)
    return out
    