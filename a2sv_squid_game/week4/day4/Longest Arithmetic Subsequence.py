class Solution:
    # 2 4 7 9 10
    # 
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # nums.sort()
        ans = 0
        memo = {}
        dp = {}
        for i in range(1, len(nums)):
            for j in range(i):
                d = nums[j] - nums[i]
                if (j, d) in memo:
                    memo[i, d] = memo[j, d] + 1
                else:
                    memo[i, d] = 2
        # print(memo)
        for i in memo:
            ans = max(ans, memo[i])
        return ans
