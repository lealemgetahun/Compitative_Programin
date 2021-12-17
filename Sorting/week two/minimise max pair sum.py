
def minPairSum(nums):
    nums.sort()
    max_sum = 0
    j = len(nums)-1
    i = 0
    
    while i < j:
        total = nums[i] + nums[j]
        # print(total)
        if total > max_sum:
            max_sum = total
        i += 1
        j -= 1
    return max_sum