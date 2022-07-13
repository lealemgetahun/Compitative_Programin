n , v = map(int,input().split)

i = 1
total = 0
gas = 0
while i < n:
    while gas < v:
        gas += 1
        total += i
    i += 1
    gas -= 1

print(total)

