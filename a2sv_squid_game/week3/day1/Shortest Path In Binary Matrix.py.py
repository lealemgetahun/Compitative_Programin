class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        queue.append((0,0))
        visited = set()
        visited.add((0,0))
        dirc = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1],[1,1],[-1,-1]]
        count = 1
        
        if grid[0][0] != 0:
            return -1
        def bound(r,c):
            return 0<= r < len(grid) and 0 <= c < len(grid)
        while queue:
            size = len(queue)
            
            for _ in range(size):
                row,col = queue.popleft()
                if (row, col) == (len(grid)-1, len(grid) -1):
                    return count
                for i in dirc:
                    r = row + i[0]
                    c = col + i[1]
                    
                    if bound(r,c) and (r,c) not in visited and grid[r][c] == 0:
                        queue.append((r,c))
                        visited.add((r,c))
                        
            count += 1
            
        return -1