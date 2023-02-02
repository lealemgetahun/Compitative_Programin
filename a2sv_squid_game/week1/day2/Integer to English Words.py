class Solution:
    def rec(self, num, dic):
        if num == 0:
            return ""
        ans = []
        if num < 20:
            ans.append(dic["0-20"][num] + " ")
        elif num < 100:
            ans.append(dic["tens"][num // 10])
            ans.append(self.rec(num % 10, dic))
        else:
            ans.append(dic["0-20"][num // 100])
            ans.append("Hundred")
            ans.append(self.rec(num % 100, dic))
        # print(ans)
        return " ".join(ans)


    def numberToWords(self, num):

        dic = {
            "0-20": ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"],
            "tens": ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety","Hundred"],
            "thousands": ["","Thousand","Million","Billion"]
        }

        if num == 0:
            return "Zero"

        ans = []
        i = 0
        while num > 0:
            rem = num % 1000
            # print(rem, i)
            if rem != 0:
                temp = self.rec(rem, dic) + dic["thousands"][i] + " "
                ans.append(temp.strip())
            num //= 1000
            i += 1
        # print(ans)
        ans = ans[::-1]
        return " ".join(ans)

    