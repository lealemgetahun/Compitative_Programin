class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        joined = []
        for i in range(len(scores)):
            joined.append((scores[i], ages[i])) 
        joined.sort()
        
        dp = [0]*(max(ages) +1)

        for score, age in joined:
            dp[age] = score + max(dp[: age + 1])

        return max(dp)
                 
