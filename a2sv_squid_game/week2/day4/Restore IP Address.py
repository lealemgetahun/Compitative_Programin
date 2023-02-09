class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(s, dot, path):
            if dot > 4:
                return 
            if dot == 4 and not s:
                ans.append(".".join(path))
                return 
            for i in range(1, len(s)+1):
                if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                    dfs(s[i:], dot+1, path+[s[:i]])

        dfs(s, 0, [])
        return ans