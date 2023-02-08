class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        graph = defaultdict(set)
        bus = defaultdict(set)
        for i in range(len(routes)):
            for route in routes[i]:
                bus[route].add(i)
                graph[route].update(routes[i])
        vis = set()
        queue = deque()
        queue.append((source, 0))
        vis.add(source)
 
        while queue:
            cur, count = queue.popleft()
            if cur == target:
                return count
            for route in graph[cur]:
                if route not in vis:
                    vis.add(route)
                    if bus[route] in bus[cur] or bus[cur] in bus[route]:
                        queue.append((route, count))
                    else:
                        queue.append((route, count + 1))

        return -1