def removeKdigits(num, k):
    out = ""
    stack = []
    for i in num:
        while stack and k>0 and stack[-1] > int(i):
            
            stack.pop()
            k -= 1
            
        stack.append(int(i))
    # print(stack)
    
    while k :
        stack.pop()
        k -= 1
        
    out = "".join(map(str,stack))
    ind = 0
    
    for i in range(len(out)):
        if out[i] != "0":
            ind = i
            break
        
    # print(ind0,ind)  
    # print(int("002"))
    # if ind0>ind:
    #     return "0"
    
    return "0" if out == ""else str(int(out[ind:]))