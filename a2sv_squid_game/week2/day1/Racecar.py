class Solution:
    def racecar(self, target: int) -> int:
        vis = set()
        # memo = {}
        # def dp(pos, speed, count):
         
        #     if pos == target:
        #         return count
        #     new_pos = pos + speed
        #     new_speed = speed * 2

        #     state = (new_pos, new_speed)
        #     ans = inf
        #     if state not in vis and new_pos >= 0:
        #         vis.add(state)
        #         ans = dp(new_pos, new_speed, count + 1)
        #     if speed > 0:
        #         if (pos, -1) not in vis and pos < 2 * target:
        #             vis.add((pos, - 1))
        #             ans = min(ans, dp(pos, -1, count + 1))
        #     else:
        #         if (pos, 1) not in vis and pos < 2 * target:
        #             vis.add((pos, 1))
        #             ans = min(ans, dp(pos, 1, count + 1))

        #     return ans
        # vis.add((0, 1))

        # return dp(0, 1, 0)
        queue = []
        vis.add((0,1))

        heappush(queue, (0, 0 ,1))
        while queue:
            count, pos, speed = heappop(queue)
            if pos == target:
                return count

            if (pos + speed, speed * 2) not in vis and pos + speed >= 0:
                vis.add((pos + speed, speed * 2))
                heappush(queue, (count + 1, pos + speed, speed *2))
            if speed > 0:
                if  (pos , -1) not in vis and pos < 2 * target:
                    vis.add((pos, -1))
                    heappush(queue, (count + 1, pos, -1))
            else:
                if (pos , 1) not in vis and pos < 2 * target:
                    vis.add((pos, 1))
                    heappush(queue, (count + 1, pos, 1))
