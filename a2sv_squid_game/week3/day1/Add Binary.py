class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        ans = []
        carry = 0
        i,j = len(a) -1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            f = 0 
            l = 0
            if i >= 0:
                f = int(a[i])
                i -= 1
            if j >= 0:
                l = int(b [j])
                j -= 1
                
            tot = f ^ l ^ carry
            carry = f & l | l & carry | f & carry
           
            ans.append(tot)
     
        return "".join(map(str,ans[::-1]))