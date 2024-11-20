'''
[-4,-3,-2]
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min = 1
        cur_max = 1

        for n in nums:
            prev_max = cur_max  
            cur_max = max(n, n * cur_max, n * cur_min)
            cur_min = min(n, n * prev_max, n * cur_min)
            res = max(res, cur_max)

        return res
