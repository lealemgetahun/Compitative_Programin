def largestNumber(nums):
    
    def larger(x,y):
        return x+y > y+x
    for i in range(len(nums)):
        nums[i] = str(nums[i])
    nums.sort()
    # largest_num = ""
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if not larger(nums[i],nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
    lar = "".join(nums)
    if lar[0]=="0":
        return "0"
    return lar
    
       
   
        
        
        