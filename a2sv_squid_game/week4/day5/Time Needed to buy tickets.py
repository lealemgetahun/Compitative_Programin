class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for i, tiket in enumerate(tickets):
            queue.append(i)

        count = 0
        while queue:
            ind = queue.popleft()
            if ind == k and tickets[ind] == 1:
                return count + 1 
            tickets[ind] -= 1
            count += 1
            if tickets[ind] > 0:
                queue.append(ind)
        return -1