def sortSentence(s):
    ls = s.split(" ")
    os = " "
    for i in range(len(ls)):
        for j in range(len(ls)):
            
            if int(ls[i][-1]) < int(ls[j][-1]):
                ls[i],ls[j] = ls[j], ls[i]
                    
    for i in range (len(ls)):
        ls[i] = ls[i][:len(ls[i])-1]
    return os.join(ls)
        