def insertionSort1(n, arr):
    # Write your code here
    t = arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i] > t:
            arr[i+1] = arr[i]
            print(*arr)
            if i == 0:
                arr[i] = t
                print(*arr)
            
        else:
            arr[i+1] = t
            print(*arr)
            break
   