class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        nums_len, queries_len = len(nums), len(queries)

        def is_a_solution(target):
            count = [0] * (nums_len + 1)
            for [l, r, v] in queries[:target]:
                count[l] += v
                count[r + 1] -= v
            for i in range(1, len(count)):
                count[i] += count[i - 1] 

            for i in range(nums_len):
                if nums[i] > count[i]:
                    return False
            return True

        l, r = 0, queries_len + 1
        while l < r:
            m = (l + r) // 2
            if is_a_solution(m):
                r = m
            else:
                l = m + 1

        return l if l < (queries_len + 1) else -1
