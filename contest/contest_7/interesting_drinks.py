
n = int(input())
x = list(map(int,input().split()))
x.sort()
q = int(input())
m = []
for i in range(q):
    m.append(int(input()))

i = 0

def search(l,r,m):
    ind = -1
    while l <= r:
        mid = l + (r-l)//2

        if x[mid] <= m:
            ind = mid
            l = mid + 1
        else :
            r = mid - 1
    return ind

for i in range(q):
    count = search(0,n-1,m[i])
    print (count + 1)



