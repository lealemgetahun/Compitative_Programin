def decodeString(self, s: str) -> str:
    stack = []
    
    for i in s:
        
        if i == "]":
            temp = ""
            val = ""
            while stack and stack[-1]!="[":
                temp = stack.pop() + temp
            
            # temp = temp[::-1]
            
            stack.pop()
            while stack and stack[-1] in "0123456789":
                val += stack.pop()
            
            val = int(val[::-1])
            temp = temp * val
            stack.append(temp)
            
            
        else:
            stack.append(i)
    
    ans = ""   
    for i in range(len(stack)):
        ans +=  stack[i]
    return ans
        