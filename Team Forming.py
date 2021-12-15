n = int(input())
arr = list(map(int,input().split()))

for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]

min_ques = 0
i = 0
while i < n:
    min_ques += (arr[i+1] - arr[i])
    i += 2
print(min_ques)