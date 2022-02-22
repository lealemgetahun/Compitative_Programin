def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    stack = []
    i = 0
    j = 0
    popped = popped[::-1]
    while i < len(pushed):
        while stack and stack [-1] == popped[-1]:
            stack.pop()
            popped.pop()
        stack.append(pushed[i])
        i+=1
    while stack and popped and stack[-1] == popped[-1]:
        stack.pop()
        popped.pop()
    # print(stack)
    # print("pop",popped)
    return False if stack else True