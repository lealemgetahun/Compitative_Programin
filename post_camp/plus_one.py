class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = [0]*(len(digits)+1)
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            tot = digits[i] + carry
            carry = tot // 10
            tot = tot % 10
            ans[i+1] = tot
        if carry:
            ans[0] = carry
        else:
            ans = ans[1:]
        return ans
            