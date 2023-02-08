class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dis = []
        for i in range(len(nums)):
            if nums[i] not in dis:
                dis.append(nums[i])
        
        if len(dis)>2:
            return sorted(dis)[-3]
        return sorted(dis)[-1]