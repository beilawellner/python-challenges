'''
nums = [2,5,7,8,9,2,3,4,3,1], k = 3
'''
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        def is_increacing(start):
            for i in range(start + 1, start + k):
                if start + k - 1 >= len(nums) or nums[i] <= nums[i - 1]:
                    return False
            return True

        for i in range(n - k + 1):
            if is_increacing(i) and is_increacing(i + k):
                return True
        return False
