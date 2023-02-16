class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        edges = set()
        edges.update([1,9,99])
        
        @lru_cache(None)
        def dp(i, prev, prev_count, k):
            if k < 0:
                return inf
            if i >= len(s):
                return 0
            ans = inf
            if s[i] == prev:
                if prev_count in edges:
                    add = 1
                else:
                    add = 0
                ans = add + dp(i+1, prev, prev_count + 1, k) 
            else:
                ans = 1 + dp(i+1, s[i], 1, k)
                ans =  min(ans, dp(i + 1, prev, prev_count, k - 1))
            return ans
            
        return dp(0, "", 0, k)
            

