
def maxOperations(nums, k):
    count = 0
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    print(dic)   
    for i in dic:
        if i <k:
            j = k-i
            if i == j and i + j == k:
                count += dic[i]//2
                print("=",count)
                if dic[i]%2==0:
                    dic[i] = 0
                else:
                    dic[i] = 1

            if i != j and j in dic:
                if dic[i] == dic[j]:
                    count += dic[i]
                    dic[i],dic[j] = 0,0

                    # del dic[i]
                    # del dic[j]

                elif dic[i] != 0 and dic[j]!=0:
                    
                    print("!",count)
                    if dic[i] >dic[j]:
                        count += dic[j]
                        dic[i] = dic[i]-dic[j]
                        dic[j] = 0
                        

                    else:
                        count += dic[i]
                        dic[i] = dic[j]-dic[i]
                        dic[i] = 0
        
                
    return count

                