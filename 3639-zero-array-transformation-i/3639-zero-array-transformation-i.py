class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        dec_count = [0] * (n + 1)
        for l, r in queries:
            dec_count[l] += 1
            dec_count[r + 1] -= 1

        cur = 0
        for i in range(n):
            cur += dec_count[i]
            if nums[i] > cur:
                return False
        return True