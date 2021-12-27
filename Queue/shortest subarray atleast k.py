import deque
def shortestSubarray(nums, k):

    sum_ = [0]*(len(nums)+1)
    ind = deque()
    res = len(nums)+1
    for i in range(len(nums)):
        sum_[i+1] = sum_[i]+nums[i]
    print(sum_)
    
    for i in range(len(sum_)):
        while ind and sum_[i] - sum_[ind[0]] >= k:
            res = min(res,i-ind.popleft())
        while ind and sum_[ind[-1]] >= sum_[i]:
            ind.pop()
        ind.append(i)
        
    if res <= len(nums):
        return res
    else:
        return -1