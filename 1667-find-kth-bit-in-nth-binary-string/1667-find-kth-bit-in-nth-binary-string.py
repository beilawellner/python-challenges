class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2**n - 1

        def helper(length, k):
            if length == 1:
                return '0'
            half = length//2
            if k <= half:
                return helper(half, k)
            if k > half+1:
                res = helper(half, 1 + (length-k))
                return '1' if res == '0' else '0'
            else:
                return '1'

        return helper(length, k)
        
        
        
        # sequence = '0'
        # while len(sequence) < k:
        #     sequence = sequence + '1' + ''.join('1' if x == '0' else '0' for x in sequence)[::-1]
        # return sequence[k-1]
