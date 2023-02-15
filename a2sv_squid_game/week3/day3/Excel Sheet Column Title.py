class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        carry = 0
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while columnNumber > 0:
            carry = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            char = letter[carry]
            ans.append(char)
   
        return "".join(ans[::-1])
        
        