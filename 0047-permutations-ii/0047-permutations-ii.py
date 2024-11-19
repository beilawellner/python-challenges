class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        res = []
        counter = Counter(nums)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in counter:
                if counter[n] > 0:
                    perm.append(n)
                    counter[n] -= 1

                    dfs()

                    counter[n] += 1
                    perm.pop()

        
        dfs()
        return res