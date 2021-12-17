
def pancakeSort(arr):
    out = []
    def flip(end):
        start = 0
        while start < end:
            arr[start],arr[end] = arr[end] ,arr[start]
            start += 1
            end -= 1
        # print(arr)  
    for i in range(len(arr)-1,-1,-1):
        m = i
        for j in range(i,-1,-1):
            # print(arr[m],arr[j])
            if arr[j] > arr[m] :
                m = j
        if m != i:
            flip(m)
            flip(i)
            out.append(m+1)
            out.append(i+1)
    return out