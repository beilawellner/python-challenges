class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        curr_sum, max_sum = 0, 0
        seen = defaultdict(int)
        start = 0

        for end in range(len(nums)):
            curr_sum += nums[end]
            if end - start == k:
                seen[nums[start]] -= 1
                if seen[nums[start]] == 0:
                    del seen[nums[start]]
                curr_sum -= nums[start]
                start += 1
            seen[nums[end]] += 1
            if end - start == k - 1 and len(seen) == k:
                max_sum = max(max_sum, curr_sum)
        return max_sum
