
def checkArithmeticSubarrays(nums, l, r) :
    out = []
            
    def arithmetic(arr):
        arr.sort()
        dif = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != dif:
                return False
        return True
    for i in range(len(l)):
        sub = nums[l[i]:r[i]+1]
        # print(sub)
        if arithmetic(sub):
            out.append(True)
        else:
            out.append(False)
            
    return out
    