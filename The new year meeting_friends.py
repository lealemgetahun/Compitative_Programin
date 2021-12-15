m,n,o = list(map(int,input().split()))
min_trip = 0
for i in m,n,o:
    if i is not min(m,n,o) and i is not max(m,n,o):
        min_trip = i - min(m,n,o) + abs(i - max(m,n,o))

print(min_trip)