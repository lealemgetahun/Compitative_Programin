class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year = 1950
        ans = year
        max_count = 0
        while year <= 2050:
            count = 0
            for start, end in logs:
                if start <= year < end:
                    count += 1
            if count > max_count:
                ans = year
                max_count = count
            year += 1
        return ans
