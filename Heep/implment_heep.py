
from operator import le


heap = []
def leftChild(ind):
    return (2*ind) + 1
def rightChild(ind):
    return (2*ind) + 2
def parent(ind):
    return (ind-1)//2

def heapify(arr, n, i,s):

    #  go upward
    j = i
    p = parent(i)
    left = leftChild(j)
    right = rightChild(j)
    if s == "up":
        while p >= 0:
            if arr[i] < arr[p]:
                temp = arr[p]
                arr[p] = arr[i]
                arr[i] = temp
            i = p
            p = parent(p)
    #  go downward
    if s == "down":

        while left < len(heap) and right < len(heap):
            if arr[left] < arr[right] and arr[left] < arr[j]:
                arr[left],arr[j] = arr[j],arr[left]
                j = left
            elif arr[right] < arr[left] and arr[right] < arr[j]:
                arr[right] , arr[j] = arr[j],arr[right]
                j = right
            left = leftChild(j)
            right = rightChild(j)

    return arr

def insert(element):
    if heap:
        index = len(heap)
        p = parent(index)

        heap.append(element)
        if element < heap[p]:
            temp = heap[p]
            heap[p] = element
            heap[index] = temp
        heapify(heap,len(heap),p,"up")
    else:
        heap.append(element)
    
    return heap


print(insert(4))
print(insert(1))
print(insert(3))
print(insert(9))
print(insert(7))
print(insert(2))
print(insert(0))


def remove(i):
    if heap:
        last = len(heap) -1
        heap[i],heap[last] = heap[last],heap[i]
        heap.pop()
    
    heapify(heap,len(heap),i,"down")
    return heap
# #Heapify function to maintain heap property.


print(remove(0))
def update(i,element):
    if heap:
        heap[i] = element
        heapify(heap,len(heap),i,"up")
        
    return heap

def getMin():
    return heap[0]

print(getMin())

print(update(3,-1))

# #Function to build a Heap from array.
# def buildHeap(self,arr,n):
#     # code here

# #Function to sort an array using Heap Sort.    
def HeapSort(arr, n):
     #code here
    res  = []
    for i in range(len(arr)):
        insert(arr[i])
    
    while heap:
        res.append(getMin())
        remove(0)
    print(res)

arr  = [10,9,8,7,6,5,4,3,2,1]   
# HeapSort(arr,0)


