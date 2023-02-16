class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        out = []
        dic = {}
        count = 0
        no = []
        if len(changed)%2 != 0:
            return []
        
        for i in changed:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        if 0 in dic:
            no = dic[0]
            if dic[0] % 2 == 0:
                out=[0]*(dic[0]//2)
                del dic[0]
            else:
                return []
            
        for i in sorted(dic):
            if i*2 in dic:
                if dic[i] > dic[i*2]:
                    return []
                elif dic[i] != 0:
                    out.extend([i]*dic[i])
                    
                    dic[i*2] = dic[i*2] - dic[i]
                    dic[i] = 0
            
                
        for  i in dic:
            if dic[i] != 0:
                return []
        
        return out