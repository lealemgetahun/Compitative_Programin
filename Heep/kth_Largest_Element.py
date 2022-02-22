import heapq
def __init__(self, k, nums):
    self.k = k
    self.minheap = nums
    heapq.heapify(self.minheap)
    while len(self.minheap) > self.k:
        heapq.heappop(self.minheap)

def add(self, val: int) -> int:
    heapq.heappush(self.minheap, val)
    if len(self.minheap) > self.k:
        heapq.heappop(self.minheap)
    return self.minheap[0]