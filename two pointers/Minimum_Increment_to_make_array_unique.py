def minIncrementForUnique(self, nums):
    stack = []
    count = 0
    
    nums.sort()
    
    for i in nums:
        # if stack and stack[-1] < i:
        #     stack.append(i)
        if stack and stack[-1] >= i:
            temp = (stack[-1] - i) + 1
            stack.append(i+temp)
            count += temp
        else:
            stack.append(i)
    print(stack)
            
    return count