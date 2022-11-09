class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        total = sum(nums)
        uniqe_sum = sum(set(nums))
        expected_sum  = n*(n+1)//2
       
        
        return [total-uniqe_sum, expected_sum-uniqe_sum]
                

        