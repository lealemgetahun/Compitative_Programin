class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:

        ans = 0
        count = s.count("01")
        while count:
            s = s.replace("01","10")
            # print(s)
            count = s.count("01")
            ans += 1
        return ans