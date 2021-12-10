def smallerNumbersThanCurrent(nums):
    out = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[j] < nums[i]:
                count += 1
        out.append(count)
    return out
        