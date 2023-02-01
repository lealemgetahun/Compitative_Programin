class Solution:
    def sumRegion(self, row1, col1, row2, col2, pref):
        ans = pref[row2+1][col2+1] - pref[row1][col2+1] - pref[row2+1][col1] + pref[row1][col1]
        return ans  
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        pref = [[0 for j in range(len(mat[0]) + 1)] for i in range(len(mat) + 1)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                pref[i + 1][j + 1] = pref[i][j + 1] + pref[i + 1][j] + mat[i][j] - pref[i][j]
        
        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[0])):
                row1, col1 = max(0, i - k), max(0, j - k)
                row2, col2 = min(len(mat) - 1, i + k), min(len(mat[0]) - 1, j + k)
                temp.append(self.sumRegion(row1, col1,row2,col2,pref))
            ans.append(temp)

        return ans
        