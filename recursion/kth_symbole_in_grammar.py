def kthGrammar(self, n: int, k: int) -> int:
        
    length = (2**(n-2))
    # mid = (length // 2)
    
    if n == 1:
        return 0
    
    if k <= length:
        return  self.kthGrammar(n-1,k)
    else:
        res = self.kthGrammar(n-1,k-length)
        return 0 if res == 1 else 1
        