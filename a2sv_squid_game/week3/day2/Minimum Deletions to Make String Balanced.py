class Solution:
    def minimumDeletions(self, s: str) -> int:
        a = s.count("a")
        b = 0
        self.ans = a
        def dp(i, a, b):
            if i > len(s):
                return a + b
            if s[i - 1] == "b":
                b += 1
            else:
                a -= 1
            t = dp(i + 1, a, b)
            self.ans = min(self.ans, a + b)
            return self.ans
        dp(1, a, b)
        return self.ans


