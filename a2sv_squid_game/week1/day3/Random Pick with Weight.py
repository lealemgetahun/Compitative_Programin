class Solution:

    def __init__(self, w: List[int]):
        self.weight = w
        n = len(w)
        self.pref = [0]*(n + 1)

        for i in range(n):
            self.pref[i + 1] = self.pref[i] + w[i]

        self.total = self.pref[-1]
        self.len = n

    def pickIndex(self) -> int:

        left = 0
        right = self.len - 1
        picked = random.randint(1,self.total)
        ans = 0
        while left <= right:
            mid = (left + right)//2
            if picked <= self.pref[mid]:
                right = mid - 1
            else:
                left = mid + 1
                ans = mid
        return ans

        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()