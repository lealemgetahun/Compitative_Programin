import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKLists(lists):
    arr = []
    new = ListNode()
    s = new
    for i in lists:
        while i:
            heapq.heappush(arr,i.val)
            i = i.next
            
    for i in range(len(arr)):
        n = ListNode(heapq.heappop(arr))
        new.next = n
        new = new.next
    return s.next