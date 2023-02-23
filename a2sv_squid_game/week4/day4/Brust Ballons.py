#Floid walshall
# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         connected = [[False for i in range (numCourses)] for i in range (numCourses)]

#         for i, j in prerequisites:
#             connected[i][j] = True
#         for k in range(numCourses):
#             for i in range(numCourses):
#                 for j in range(numCourses):
#                     if connected[i][k] and connected[k][j]:
#                         connected[i][j] = True
#         ans = []
#         for u, v in queries:
#             ans.append(connected[u][v])
#         return ans

class Solution:S
    def maxCoins(self, nums: List[int]) -> int:

        dp = [[0 for i in range(len(nums) + 2)] for i in range(len(nums) + 2) ]
        nums = [1] + nums
        nums.append(1)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 2, len(nums)):
                for k in range(i + 1, j):
                    val = nums[i]*nums[k]*nums[j]
                    dp[i][j] = max(val + dp[i][k] + dp[k][j], dp[i][j])

        return dp[0][len(nums) -1]
