
def reverseParentheses(s):
    out = list(s)
    stack = []
    o = ""
    for i in range(len(out)):
        if out[i] == "(":
            stack.append(i)
        elif out[i] == ")":
            if stack:
                x = stack.pop()
                temp = out[x+1:i]
                temp = temp[::-1]
                out[x+1:i] = temp
    for i in out:
        if i not in "()":
            o += i
            
            
    return o
                        
    