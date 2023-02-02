class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        unique = set(nums)
        if 0 in unique:
            unique.remove(0)

        return len(unique)