def longestSubarray(self, nums: List[int], limit: int) -> int:
    min_queue =deque()
    max_queue = deque()
    i  = 0
    j = 0
    count = 0
    while j < len(nums):
        while min_queue and nums[j] <= nums[min_queue[-1]]:
            min_queue.pop()
        while max_queue and nums[j] >= nums[max_queue[-1]]:
            max_queue.pop()
        min_queue.append(j)
        max_queue.append(j)
        
        while nums[max_queue[0]] - nums[min_queue[0]] > limit:
            i += 1
            if i > min_queue[0]:
                min_queue.popleft()
            if i > max_queue[0]:
                max_queue.popleft()
        
        count = max(count, j - i + 1)
        j += 1
            
    return count