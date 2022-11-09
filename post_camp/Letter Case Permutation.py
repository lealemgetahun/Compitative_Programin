class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        self.ans = []
        self.backtrack(s, "", 0)
        return self.ans

    def backtrack(self, s, path, i ):
        if len(path) == len(s):
            self.ans.append(path)
        else:
            if s[i].isalpha():
                self.backtrack(s, path + s[i].swapcase(), i + 1)
            self.backtrack(s, path + s[i], i + 1)
    
                