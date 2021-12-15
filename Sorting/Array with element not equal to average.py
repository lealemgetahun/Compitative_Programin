class Solution:
    def rearrangeArray(self, nums) :
        out=[0]*len(nums)
        nums.sort()
        m = nums[len(nums)//2]
        i = 0
        j = 1
        k = 0
        while(i < len(nums)):
            if nums[i] < m:
                out[j] = nums[i]
                j+=2
            i += 1
        v = 0
        while(v < len(nums)):
            if nums[v] >= m:
                out[k] = nums[v]
                k+=2
            v += 1
            
        return out