class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(x == 0 for x in nums):
            return \0\
        
        nums = [str(num) for num in nums]

        def compare(num1, num2):
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return \\.join(nums)