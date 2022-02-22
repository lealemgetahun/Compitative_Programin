def fib(self, n: int) -> int:
    f = 0
    
    if n == 0:
        f += 0
    elif n == 1:
        f += 1
    else:
        f  = self.fib(n-1) + self.fib(n-2)

    return f
            