'''
nums = [2,5,7,8,9,2,3,4,3,1]
dp = [1,1,2,3,4,5,1,2,3,1,1]
max_len_subset = 1
'''
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n + 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1

        max_len_subset = 1
        for i in range(1, n):
            prev_end = i - dp[i]

            if prev_end >= 0:
                max_len_subset = max(max_len_subset, min(dp[prev_end], dp[i]))
            max_len_subset = max(max_len_subset, dp[i] // 2)

        return max_len_subset
