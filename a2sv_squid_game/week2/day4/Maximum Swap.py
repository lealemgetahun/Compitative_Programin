class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        ans = int("".join(num))
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                num[i], num[j] = num[j], num[i]
                n = int("".join(num))
                if n > ans:
                    ans = n
                num[i], num[j] = num[j], num[i]
        return ans
        