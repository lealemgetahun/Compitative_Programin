class Solution:
    def check(self, s, word):
        i = 0
        j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:

                count = 1
                prev = s[i]
                prev_w = word[j]
                cnt = 1
                while i + 1< len(s) and  s[i + 1] == prev:
                    count += 1
                    i += 1
                while j +1< len(word) and word[j + 1] == prev_w:
                    cnt += 1
                    j += 1
                if count == cnt or count - cnt >= 2:
                    # print(s[i], word[j], count, cnt)
                    i += 1
                    j += 1
                elif cnt > 1 and count - cnt >= 0:
                    i += 1
                    j += 1
                else:
                    return False
                
            else:
                return False
        if i < len(s) or j < len(word):
            return False
        return True
               

    def expressiveWords(self, s: str, words: List[str]) -> int:
        count = 0
        for word in words:
            count += self.check(s, word)
        return count