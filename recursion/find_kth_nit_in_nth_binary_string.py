def findKthBit(self, n: int, k: int) -> str:
    x = (2**n) - 1
    l = (x // 2) + 1
    
    
    if n == 1:
        return "0"
    if l == k:
        return "1"
    if k < l:
        return self.findKthBit(n-1,k)
        
    else: 
        res = self.findKthBit(n-1,(x-k)+1)
        return "0" if res == "1" else "1"