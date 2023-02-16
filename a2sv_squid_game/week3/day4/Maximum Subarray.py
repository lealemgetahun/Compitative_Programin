class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
 
        ans = nums[0]

        prev = nums[0]
        for n in nums[1:]:
            prev = max(n, prev + n)
            ans = max(prev, ans)
        return ans
            
    
    