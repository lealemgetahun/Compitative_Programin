class Solution:
    def inBound(self, i, j, grid):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        start = (0, 0)
        key = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    start = (i, j)
                elif grid[i][j].islower():
                    key += 1
        queue = deque()
        queue.append((0, start, tuple()))
        vis = set()
        directions = [[0,1], [1, 0], [-1, 0], [0, -1]]
        ans = -1
        while queue:
            dis, (i,j) , found = queue.popleft()
            if (i, j, found) not in vis:
                vis.add((i, j,found))
                for dx, dy in directions:
                    found_keys = set(found)
                    row, col = i + dx, j + dy
                    if len(set(found)) == key:
                        return dis
                    if self.inBound(row, col, grid) and grid[row][col] != "#":
                        if grid[row][col].isupper() and grid[row][col].lower() not in found_keys:
                            continue 
                        if grid[row][col].islower():
                            found_keys.add(grid[row][col])
                            queue.append((dis+1, (row,col), tuple(found_keys)))
                        else:
                            queue.append((dis + 1, (row, col), tuple(found_keys)))
                      
        return ans
