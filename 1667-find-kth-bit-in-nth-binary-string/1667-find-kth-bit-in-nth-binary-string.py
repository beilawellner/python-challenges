class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        sequence = '0'
        while len(sequence) < k:
            sequence = sequence + '1' + ''.join('1' if x == '0' else '0' for x in sequence)[::-1]
        return sequence[k-1]
