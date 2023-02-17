class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        a = set()
        for  i in range(len(s)):
            if s[i] in dic:
                a.add(s[i])
            else:
                dic[s[i]] = i
                
        ind = inf
        for i in dic:
            if i not in a:
                ind = min(ind, dic[i])
        return ind if ind != inf else -1