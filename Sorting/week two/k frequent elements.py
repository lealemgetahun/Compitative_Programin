
def topKFrequent( nums, k: int):
    dic = {}
    out=[]
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    sort = sorted(dic.items(), key=lambda item: item[1])
    n= len(sort) -1
    while n >= 0:
        out.append(sort[n][0])
        n -= 1
    print(out)
    return out[:k]
        