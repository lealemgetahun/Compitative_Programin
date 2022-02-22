def frequency(nums,k):
    # print(nums)
    dic = {}
    freq = 0
    n_freq = 0

    for i in nums:
        if i in dic:
            dic[i] += 1
            if dic[i] > freq:
                freq = dic[i]
    
        else:
            dic[i] = 1
            if dic[i] > freq:
                freq = dic[i]
        if freq <= dic[i]:
            if n_freq < i:
                n_freq = i
    print(dic)
    print(freq)
    count = 1
    for i in dic:
        if k and i < n_freq:
            if n_freq - i <= k:
                k -= n_freq - i
                count += 1
            
    print(count)

a = [1,2,4]
b = [1,4,8,13]
c = [3,9,6,6]

frequency(c,2)