class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr_sum, max_sum = 0, 0
        prev_idx = {}
        start = 0

        for end in range(len(nums)):
            curr_sum += nums[end]

            i = prev_idx.get(nums[end], -1)

            while start <= i or end - start + 1 > k:
                curr_sum -= nums[start]
                start += 1

            if end - start + 1 == k:
                max_sum = max(max_sum, curr_sum)

            prev_idx[nums[end]] = end

        return max_sum
