class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        product = 1
        for i in range(n):
            res.append(product)
            product *= nums[i]
        product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= product
            product *= nums[i]
        return res


    # # two arrays
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     prefix = [1] * n
    #     sufix = [1] * n

    #     for i in range(1, n):
    #         prefix[i] = prefix[i - 1] * nums[i - 1]
    #     for i in range(n - 2, -1, -1):
    #         sufix[i] = sufix[i + 1] * nums[i + 1]

    #     return [prefix[i] * sufix[i] for i in range(n)]
