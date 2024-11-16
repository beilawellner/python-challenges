'''
nums = [1,2,3,4,3,2,5], k = 3
          l
          r
'''
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        seq_count = 1

        for r in range(len(nums)):
            if r > 0 and nums[r - 1] + 1 == nums[r]:
                seq_count += 1
            if r - l + 1 > k:
                if nums[l] + 1 == nums[l + 1]:
                    seq_count -= 1
                l += 1
            if r - l + 1 == k:
                res.append(nums[r] if seq_count == k else -1)

        return res
