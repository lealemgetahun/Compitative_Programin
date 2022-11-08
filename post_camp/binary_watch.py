class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        ans = []
        num_of_2_bit = []

        for i in range(60):
            num_of_2_bit.append( bin(i).count("1"))

        for hour in range(12):
            hour_day = num_of_2_bit[hour]
            for i in range(60):
                mb = num_of_2_bit[i]
                if hour_day + mb == turnedOn:
                    ans.append(f"{hour}:{i:02d}")
        return ans