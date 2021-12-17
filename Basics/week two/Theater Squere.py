import math
n,m,a = list(map(int,input().split()))
length = math.ceil(n/a)
width = math.ceil(m/a)
print(length*width)