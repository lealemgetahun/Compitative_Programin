class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        first_XOR, sec_XOR, ind = 0, 0, 0
        for n in nums:
            first_XOR ^= n
            
        for i in range(32):
            if first_XOR & 1 << i:
                ind = i
                break
        for n in nums:
            if n & 1 << ind:
                sec_XOR ^= n
        return [first_XOR ^ sec_XOR, sec_XOR]