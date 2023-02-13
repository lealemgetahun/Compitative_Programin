class AllOne:

    def __init__(self):
        self.dic = defaultdict(int)
        self.min_heap = []
        self.max_heap = []

    def inc(self, key: str) -> None:
        self.dic[key] += 1
        heappush(self.min_heap, (self.dic[key], key))
        heappush(self.max_heap, (-self.dic[key], key))
        
    def dec(self, key: str) -> None:
        self.dic[key] -= 1
        if self.dic[key] > 0:
            heappush(self.min_heap, (self.dic[key], key))
            heappush(self.max_heap, (-self.dic[key], key))
        
    def getMaxKey(self) -> str:
        while self.max_heap:
            if -self.max_heap[0][0] == self.dic[self.max_heap[0][1]] and self.dic[self.max_heap[0][1]] > 0:
                return self.max_heap[0][1]
            else:
                heappop(self.max_heap)
        return ""
    def getMinKey(self) -> str:

        while self.min_heap:
            if self.min_heap[0][0] == self.dic[self.min_heap[0][1]] and self.dic[self.min_heap[0][1]] > 0:
                return self.min_heap[0][1]
            else:
                heappop(self.min_heap)
        return ""



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()