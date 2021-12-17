
def minSetSize(arr):
    dic = {}
    out=[]
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    sort = sorted(dic.items(), key=lambda item: item[1])
    l = len(arr)/2
    s = 0
    count = 0
    for i in range(len(sort)-1,-1,-1):
        s += sort[i][1]
        print(s)
        count += 1
        if s >= l:
            break
    return count
        