class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        res = 0
        for num in list(count.keys()):
            if num * 2 == k:
                # Count pairs where both elements are the same
                res += count[num] // 2

            elif num < k - num and k - num in count:
                # Count pairs (num, k-num) ensuring each pair is counted once
                res += min(count[num], count[k - num])
                
        return res
