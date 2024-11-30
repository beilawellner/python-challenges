'''
nums = [2,5,7,8,9,2,3,4,3,1], k = 3
        s
            i
last_start = 0
subsets_starts = {0,1,2}
'''
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        subsets_start = set()
        start = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                start = i
            if i - start + 1 == k:
                if start - k in subsets_start:
                    return True
                subsets_start.add(start)
                start += 1
        return False
