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
            "0-20": {0:"",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"},
            "tens": {0:"",1:"Ten",2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety",10:"Hundred"},
            "thousands": {0:"",1:"Thousand",2:"Million",3:"Billion"}
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

    