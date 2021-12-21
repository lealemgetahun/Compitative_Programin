def evalRPN(tokens):
    res = 0
    stack = []
    oprators = "+-*/"
    
    for i in tokens:
        x =0
        y =0
        if i in oprators: 
            if stack:
                x= stack.pop()
                y = stack.pop()
                if i == "+":
                    res = x+y
                    stack.append(res)
                    # print("+",res)
                elif i == "-":
                    
                    res = y-x
                    stack.append(res)
                    # print("-",res)
                elif i == "*":
                    
                    res =x*y
                    stack.append(res)
                    # print("*",res)
                elif i == "/":
                    
                    res = int(y/x)
                    stack.append(res)
                    # print("/",res)
        else:
            stack.append(int(i))
    
    return stack[-1]
    