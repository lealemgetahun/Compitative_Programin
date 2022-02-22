def myPow(self, x: float, n: int) -> float:
        
    total = 0
    if n < 0:
        x = 1/x
        n = -n
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        if n % 2 == 0:
            total = self.myPow(x,n//2)
            # print("t",total*total)
            return total*total
        else:
            total = self.myPow(x,(n//2))
            res = total * total * x
        
            return res
        