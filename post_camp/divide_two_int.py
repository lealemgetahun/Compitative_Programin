class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)
        
        ans = 0
        tot = divisor
        while tot <= dividend:
            cur = 1
            while (tot + tot) <= dividend:
                tot += tot
                cur += cur
            dividend -= tot
            tot = divisor
            ans += cur
        # print(2**31) 
        return min(2147483647, max(-ans if neg else ans, -2147483648))
        