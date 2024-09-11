class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, max_len = 0, 0
        
        for end in range(len(nums)):
            if nums[end] == 0:
                k -= 1
            
            while k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1
            
            max_len = max(max_len, end - start + 1)
        
        return max_len
