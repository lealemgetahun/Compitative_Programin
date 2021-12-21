class MyCircularDeque:

    def __init__(self, k: int):
        self.len = k
        self.deque = []

    def insertFront(self, value: int) -> bool:
        
        if self.len == 0:
            return False
        elif self.len > 0:
            self.deque.insert(0,value)
            self.len -= 1   
        return True

    def insertLast(self, value: int) -> bool:
        
        if self.len == 0:
            return False
        elif self.len > 0:
            self.deque.append(value)
            # print(self.len)
            self.len -= 1
            # print(self.len)
       
        return True

    def deleteFront(self) -> bool:
        if self.deque:
            self.len += 1
            self.deque.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.deque:
            self.len += 1
            self.deque.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1
        
        

    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.deque:
            return False
        return True

    def isFull(self) -> bool:
        if self.len == 0:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()