from collections import deque
n,l,r = list(map(int,input().split()))
ans = []
def sam(n):
    
    if n == 1:
        ans.append(1)
        return ans
    if n % 2 == 0:
        # ans.append(0)
        ans.extend(sam(n // 2))
        return ans
    else:
        # ans.append(1)
        ans.extend(sam(n // 2))
        return ans
    # n = n // 2
    # ans.append(sam(n))

  
    
        

print(sam(n))

