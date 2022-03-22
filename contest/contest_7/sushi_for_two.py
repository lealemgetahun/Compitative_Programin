n = int(input())
t = list(map(int,input().split()))

count = 0
tuna = 0
eel = 0

i = 0
j = 0

arr = []
while j < len(t):
    if t[i] == t[j]:
        count += 1
        j += 1
    else:
        arr.append(count)
        i = j
        j = j
        count = 0
arr.append(count)
    

for i in range(len(arr)-1):
    tuna = (min(arr[i],arr[i+1]))*2
    eel = max(eel,tuna)
print(eel)

# def search (arr):
#     l = 0
#     r = len(arr)

#     while l <= r:
#         mid = l + (r-l)//2

#         tuna = 0
#         eel = 0

#         if 


