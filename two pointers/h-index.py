def hIndex(self, citations) -> int:
        l = len(citations)
        citations.sort()
        # print(citations)
        c = 0
        for i in range(l):
            if citations[i] >= l-i:
                c = i+1
                break
            
        return 0 if c == 0 else l-(c-1)