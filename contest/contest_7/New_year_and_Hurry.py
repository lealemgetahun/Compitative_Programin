n,k = list(map(int,input().split()))

min_left = 240 - k
count = 0
i = 1
total = 0
while i <= n:
    
    if total + i*5 > min_left:
        break
    total += i*5
    count += 1
    i += 1
print(count)

