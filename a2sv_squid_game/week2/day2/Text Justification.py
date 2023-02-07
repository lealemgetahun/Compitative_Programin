class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        cur = 0
        i = 0
        j = 0
        while i < len(words):
            path = []
            cur = len(words[i]) + 1
            count = 0
            while cur <= maxWidth + 1 and j < len(words):     
                path.append(words[j])
                count += len(words[j]) + 1
                j += 1
                if j < len(words):
                    cur += len(words[j]) + 1
            i = j 
            ans.append([path,count -1, len(path)- 1])
            cur = 0
        res = []

        for i in range(len(ans) -1):
            space = ans[i][2]
            ava = 0
            add = 0
            if space:
                ava = (maxWidth - ans[i][1]) % space
                add = (maxWidth - ans[i][1]) // space
            else:
                add = (maxWidth - ans[i][1])
        
            path = []
            for j in range(len(ans[i][0]) - 1):
                path.append(ans[i][0][j])
                path.append(" ")
                if ava:
                    path.append(" "*(add + 1))
                    ava -= 1
                else:
                    path.append(" "*(add))
            path.append(ans[i][0][-1])
            if not space:
                path.append(" "*(add))
            
            res.append("".join(path))
        for i in range(len(ans) - 1, len(ans)):
            path  = []
            for j in range(len(ans[i][0]) - 1):
                path.append(ans[i][0][j])
                path.append(" ")

            path.append(ans[i][0][-1])
            path.append(" "*(maxWidth - ans[i][1]))
            res.append("".join(path))

        return res
        
                    
            





