class Solution:
    def numberOfWays(self, s: str) -> int:

        dic = defaultdict(int)
        count = 0
        for i in range(len(s)):
            dic[s[i]] += 1
            if s[i] == "0": 
                dic["10"] += dic["1"]
                dic["010"] += dic["01"]
            else: 
                dic["01"] += dic["0"]
                dic["101"] += dic["10"]

        count = dic["010"] + dic["101"]
        return count

        