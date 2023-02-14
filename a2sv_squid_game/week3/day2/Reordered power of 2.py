class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        dic = {}
        
        for i in str(n):
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            
        for j in range(30):
            dic2 = {} 
            temp = 2 ** j
            for i in str(temp):
                if i in dic2:
                    dic2[i] += 1
                else:
                    dic2[i] = 1
            
            if dic == dic2:
                return True
        return False
            
            