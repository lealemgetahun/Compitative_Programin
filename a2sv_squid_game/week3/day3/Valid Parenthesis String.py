class Solution:
    def checkValidString(self, s: str) -> bool:
        total = openb = close = 0 
        
        for i in range(len(s) - 1, -1, -1):
            
            if s[i] == '*':
                total += 1
            elif s[i] == '(':
                openb += 1
            elif s[i] == ')': 
                close += 1
            if total - openb + close < 0: 
                return False
        total = openb = close = 0
        for i in range(len(s)):
            if s[i] == '*':
                total += 1
            elif s[i] == '(': 
                openb += 1
            elif s[i] == ')': 
                close += 1
            if total + openb - close < 0: 
                return False 
        return True