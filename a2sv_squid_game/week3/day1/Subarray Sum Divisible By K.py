
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        dic = defaultdict(int)
        dic[0] = 1
        count = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total % k in dic:
                count += dic[total % k]
            dic[total % k] += 1
        return count

