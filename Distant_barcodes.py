def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
    freq= collections.defaultdict(int)
    maxFreq = 0
    for code in barcodes:
        freq[code] += 1
        if freq[code] > freq[maxFreq]:
            maxFreq = code
        
    n = len(barcodes)
    idx = 0
    out = [0]*n
        
	
    for i in range(freq[maxFreq]):
        out[idx] = maxFreq
        idx += 2
        
    del freq[maxFreq]
        
    for i,j in freq.items():
        for _ in range(j):
            if idx >= n:
                idx = 1
            out[idx] = i
            idx += 2
                
    return out