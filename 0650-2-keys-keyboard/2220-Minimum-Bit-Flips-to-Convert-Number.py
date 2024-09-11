class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_res = start ^ goal
        res = bin(xor_res).count('1')
        return res