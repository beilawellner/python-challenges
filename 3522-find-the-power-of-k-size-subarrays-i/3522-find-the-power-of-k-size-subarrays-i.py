class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        results = []
        start = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1] + 1:
                start = i
            if i >= k - 1:
                if i - start + 1 >= k:
                    results.append(nums[i])
                else:
                    results.append(-1)

        return results
