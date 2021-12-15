class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        dic = {}
        out = []
        for i in nums:
            if len(i) in dic:
                dic[len(i)].append(i)
            else:
                dic[len(i)] = [i]
        
        for i in dic:
            dic[i].sort()
        
        for i in sorted (dic.keys()):
            out.extend(dic[i])
        print(out)   
        kth = len(nums) - k
        
        return str(out[kth])