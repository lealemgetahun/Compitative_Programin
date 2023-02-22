class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:


        dic = defaultdict(int)
        count = 0
        for i in range(len(time)):
            # print(dic)
            if time[i] % 60 == 0:
                count += dic[0]
                dic[0] += 1
            else:
                if 60 - time[i] % 60 in dic:
                    count += dic[abs(60 - time[i] % 60)]
                dic[time[i] % 60] += 1
        return count 
