
t = int(input())
  
ans = []
for i in range(t):
    n,h = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    k = 0
    r = h
    l = 1

    max_move = []

    for i in range(n-1):
        max_move.append(arr[i+1]-arr[i])
    # max_move.append(arr[-1])
    

    while l <= r:
        mid = l + (r-l)//2
        
        total = mid

        for i in range(len(max_move)):
            total += min(mid,max_move[i])
        
        if total > h:
            k = mid
            r = mid - 1
        elif total < h:
            l = mid + 1
        else:
            k = mid
            break

        
    print(k)




