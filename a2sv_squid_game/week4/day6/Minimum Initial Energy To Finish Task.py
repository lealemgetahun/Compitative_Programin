class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)

        energy = tasks[0][1]
        start = energy
        for act, req in tasks:
            if req > energy:
                start += req - energy
                energy = req
            energy -= act
        return start
