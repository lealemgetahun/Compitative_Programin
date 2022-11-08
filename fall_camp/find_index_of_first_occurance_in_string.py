class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        j = len(needle)
        
        i = 0
        while j <= len(haystack):
            if haystack[i:j] == needle:
                return i
            else:
                i += 1
                j += 1
                
        return -1