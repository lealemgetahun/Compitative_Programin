class Solution:
    def valid(self, i, nums, path):
        if i > 0 and nums[i] == nums[i -1]:
            return False
        if path:
            num = path[-1] + nums[i]
            if not pow(int(sqrt(num)), 2) == num:
                return False
        return True

    def numSquarefulPerms(self, nums: List[int]) -> int:
        ans = []
    
        def backTracking(nums, path):
            if not nums:
                ans.append(path)
            for i in range(len(nums)):
                i
                if self.valid(i, nums, path):
                    backTracking(nums[:i]+nums[i+1:], path+[nums[i]])

        nums.sort()
        backTracking(nums, [])
        return len(ans)
        
        