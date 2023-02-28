class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        max_freq= 0
        for num in nums:
            freq[num] += 1
            max_freq = max(max_freq, freq[num])

        dic = defaultdict(int)
        left = 0
        ans = len(nums)
        for right in range(len(nums)):
            dic[nums[right]] += 1
            while left < len(nums) and dic[nums[right]] == max_freq:
                ans = min(right - left + 1, ans)
                dic[nums[left]] -= 1
                left += 1      
        return ans

            