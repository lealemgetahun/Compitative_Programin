def partitionLabels(self, s: str):
    
    dic = {}
    ans = []
    
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]][1] = i
        else:
            dic[s[i]] = [i,i]

    arr = list(dic.keys())
    
    cur = dic[arr[0]]
    max_val = dic[arr[0]][1]
    
    for i in range(1,len(arr)):
        if max_val > dic[arr[i]][0]:
            max_val = max(max_val,dic[arr[i]][1])
            
            continue
        else: 
            ans.append(dic[arr[i]][0] - cur[0])
            cur = dic[arr[i]]
            max_val = cur[1]
    ans.append(max_val + 1 - cur[0])
    return ans
