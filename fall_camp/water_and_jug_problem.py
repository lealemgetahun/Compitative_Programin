class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity == targetCapacity or jug2Capacity == targetCapacity:
            return True
        if (jug1Capacity + jug2Capacity) < targetCapacity:
            return False 
        return targetCapacity % gcd(jug1Capacity , jug2Capacity) == 0 