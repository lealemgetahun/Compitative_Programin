class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        j = 0
        size = 0
        ans = float('inf')
        n = len(blocks)
        for i in range(n):
            if blocks[i] == 'W':
                size += 1
            if (i - j +1) >= k :
                ans = min(ans,size)
                if blocks[j] == 'W':
                    size -= 1
                j+=1
            
        return ans 
    
