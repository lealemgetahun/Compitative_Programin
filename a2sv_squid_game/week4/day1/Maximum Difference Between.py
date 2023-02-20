class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_dif = -1
        pref_min = inf

        for num in nums:
            if num > pref_min:
                max_dif = max(max_dif, num - pref_min)
            else:
                pref_min = num
        return max_dif

