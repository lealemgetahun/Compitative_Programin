class Solution: 
    def select(self, arr, i):
        min_val= arr[i]
        num = i
        for j in range(i,len(arr)):
            if min_val>arr[j]:
                min_val=arr[j]
                num=j
        
        return min_val,num
    
    
    def selectionSort(self, arr,n):
        for i in range (n):
            min_val,num=self.select(arr,i)
            arr[num],arr[i]=arr[i],min_val
        return arr