def maxCoins(piles):
    piles.sort()

    i =0 
    j = len(piles)-1
    my = 0
    while i < j:
    
        my += piles[j-1]
        j -= 2
        i += 1
        
    print(my)
    return my
    
maxCoins([2,4,5])    
maxCoins([2,4,1,2,7,8])
maxCoins([9,8,7,6,5,1,2,3,4])