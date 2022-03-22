from collections import deque
def bfs(num,k):
    queue, size = deque([num]), 1
    count = 0
    visited = set()
    visited.add(num)
    while queue:
        
        for i in range(size):
            index = queue.popleft()
            
            if index == k:
                    return count
            left = index - 1
            right = index + 4
            
            if left not in visited:
                visited.add(left)
                queue.append(left)
                
            if right not in visited:
                visited.add(right)
                queue.append(right)
                    
                # print(queue)
        size = len(queue)           
        count += 1
    return -1

print("31", bfs(31,40))
print("31", bfs(32,40))


