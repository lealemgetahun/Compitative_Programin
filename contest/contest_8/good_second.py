n , m = list(map(int,input().split()))
stud = list(map(int,input().split()))

stud.sort()

def search(k):
    l = 0
    r = len(stud) -1
    ind = -1
    while l <= r:
        mid = l + (r-l)//2

        if stud[mid] >= k:
            ind = mid
            r = mid - 1
            
        else :
            l = mid + 1
    return ind


for i in range (n):
    dif = int(input())
    l = search(dif)

    length = len(stud[:l+1])
    
    if m % 2 == 0:
        if length > m//2 and length < m:
            print("YES")
        else:
            print("NO")
    else:
        if length >= m//2 or length < m:
            print("YES")
        else:
            print("NO")

    
    


