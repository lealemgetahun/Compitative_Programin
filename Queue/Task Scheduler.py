
def leastInterval(self, tasks: List[str], n: int) -> int:

    dic = {}
    out = []
    f = tasks[0]
    no = 0
    for i in tasks:
        if i in dic:
            dic[i] += 1
            if dic[i] > dic[f]:
                f = i
        else:
            dic[i] = 1
    
    for i in dic:
        if dic[i] == dic[f]:
            no += 1
    i = 0
    
    while dic[f] > 0:
        if dic[f] == 1:
            out.append(f)  
        else:
            out.append(f)
            out.extend(["idle"]*n)
        i += n + 1
        dic[f] -= 1

    # print(len(out)+no-1) 
    count = len(out) + no-1
    
    if count < len(tasks):
        return len(tasks)
    return count
    
            
            
            