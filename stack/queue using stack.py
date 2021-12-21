class MyQueue:


    def __init__(self):
        self.stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.pop_stack) == 0:
            for i in range (len(self.stack)):
                self.pop_stack.append(self.stack.pop())
    def pop(self) -> int:
        
        return self.pop_stack.pop()

    def peek(self) -> int:
        
        return self.pop_stack[-1]

    def empty(self) -> bool:
        if self.stack or self.pop_stack:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()