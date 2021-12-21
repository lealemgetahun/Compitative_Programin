def nextGreaterElement(nums1, nums2):
    dic = {}
    out = []
    stack = []
    stack.append(nums2[0])
    for i in range(1,len(nums2)):
        if stack[-1] < nums2[i]:
            while stack and stack[-1] <nums2[i]:
                x = stack.pop()
                dic[x] = nums2[i]
            stack.append(nums2[i])
        else:
            # x = stack.pop()
            dic[nums2[i]] = -1
            stack.append(nums2[i])
    # print(stack)
    while stack:
        dic[stack.pop()] = -1
    for i in nums1:
        out.append(dic[i])
    # print(dic)
    return out
    
        