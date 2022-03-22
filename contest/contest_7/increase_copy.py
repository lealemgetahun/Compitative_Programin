import math
t = int(input())

for i in range(t):

    n = int(input())
    mid = int(math.sqrt(n))
    min_move = float("inf")
    
    for i in range(1, mid + 1):
        op = (i - 1) + (n // i)
        if n % i == 0:
            op -= 1
        min_move = min(min_move, op)    
        
    print(min_move)