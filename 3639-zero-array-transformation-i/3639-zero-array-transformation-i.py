class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        dec_count = [0] * (n + 1)
        for l, r in queries:
            dec_count[l] += 1
            dec_count[r + 1] -= 1
        for i in range(1, n):
            dec_count[i] += dec_count[i - 1]
        for i in range(n):
            nums[i] = nums[i] - dec_count[i]
        return all(n <= 0 for n in nums)
