def countingSort(arr):
    # Write your code here
    count = [0]*100
    for i in range(len(arr)):
        count[arr[i]] += 1
    return count