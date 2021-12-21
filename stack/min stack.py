class MinStack:

    def __init__(self):
        self.stack = []
        
       
    def push(self, val: int) -> None:
        temp = self.getMin()
        if temp == None or  val < temp:
            temp = val   
        self.stack.append((val,temp))

    def pop(self) -> None:   
        self.stack.pop()

    def top(self) -> int:
        # print(self.stack)
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1] 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()