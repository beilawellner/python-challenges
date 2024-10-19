class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev = '0'
        for i in range(n):
            prev = prev + '1' + ''.join('1' if x == '0' else '0' for x in prev)[::-1]
        return prev[k-1]
