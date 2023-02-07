class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        freq = [0] * (2 * (10001) + 1)
        for num in nums:
            freq[num + 10001] += 1
        for i in range(len(freq) - 1, -1, -1):
            count += freq[i]
            if count >= k:
                return i - 10001