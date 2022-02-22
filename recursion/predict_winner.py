def PredictTheWinner(self, nums: List[int]) -> bool:
    n= len(nums)-1
    
    if self.pridict(nums,0,n,1) >= 0:
        return True
    return False

def pridict(self,nums,start,end,turn):
    if start == end:
        return turn * nums[start]
    
    p1 = turn * nums[start] + self.pridict(nums,start+1,end,-turn)
    
    p2 = turn * nums[end] + self.pridict(nums,start,end-1,-turn)
    
    # print(p1,p2)
    res = turn * max(turn * p1, turn * p2)
    
    return res