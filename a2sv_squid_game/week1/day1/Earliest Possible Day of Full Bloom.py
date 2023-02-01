class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:

        joined = [[ growTime[i], plantTime[i]] for i in range(len(plantTime))]
        joined.sort(reverse = True)
        ans = 0
        day = 0
        for grow, plant in joined:
            ans = max(ans, day + plant + grow)
            day += plant
        return ans