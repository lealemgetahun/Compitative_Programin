import heapq
def topKFrequent(words, k):
    dic = {}
    out=[]
    res = []
    for i in words:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic:
        heapq.heappush(out,(-dic[i],i))
    for i in range(k):
        res.append(heapq.heappop(out)[1])
    
    return res