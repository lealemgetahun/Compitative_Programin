class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        start = -1
        for i in graph:
            if len(graph[i]) == 1:
                start = i
                break
        vis = set()
        ans = []
        def dfs(i):
            ans.append(i)
            vis.add(i)
            for v in graph[i]:
                if v not in vis:
                    dfs(v)
        dfs(start)
        return ans

        
        
