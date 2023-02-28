class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        dp = [[0 for i in range(len(matrix[0]) + 1)] for j in range(len(matrix) + 1)]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i][j],dp[i+ 1][j]) + 1
                    ans= max(ans, dp[i+ 1][j +1])
        return ans ** 2