
def returns(s):
    ans = ""
    stack = []
    i = 0
    for i in range(len(s)):
        # print(stack)
        if stack :
            if s[i] != stack[-1][0]:
                stack.append((s[i],i))

            else:
                if stack[-1][1] == i - 1:
                    stack.pop()
        else:
            stack.append((s[i],i))
        
           
    while stack:
        if stack[-1][0] not in ans:
            temp = stack.pop()
            ans += temp[0]
        else:
            stack.pop()
        
    return ans

m = list(map(str,input().split()))
m = m [1:]
for i in m:
    sol = returns(i)
    res = sorted(sol)
    print ("".join(res))
