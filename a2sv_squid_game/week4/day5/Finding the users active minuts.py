class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = defaultdict(int)
        vis = set()
        for ids, time in logs:
            if (ids, time) not in vis:
                vis.add((ids, time))
                users[ids] += 1
        ans = [0]*k

        uam = defaultdict(int)
        for ids in users:
            uam[users[ids]] += 1
        for i in range(k):
            ans[i]= uam[i + 1]

        return ans