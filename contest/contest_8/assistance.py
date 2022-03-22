from collections import deque
import queue
n , m = list(map(int,input().split()))
visited = set()
queue = deque()
def bfs(a,b):
    queue.append(a)
    visited.add(a)
    while queue:
        cur = queue.popleft()
        if cur == n-1:
            return True
        for i in range(a,b+1):
            if i not in visited:
                visited.add(i)
    return False
arr = []  
max_day = 0 
for i in range(m):
    a,b = list(map(int,input().split()))
    if b > max_day:
        max_day = b
    bfs(a,b)
# print(visited)
if len(visited) == n:
    print("NO")
else:
    print("YES")




