def targetIndices( nums, target):
    out = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    for i in range(len(nums)):
        if nums[i] == target:
            out.append(i)
    return out