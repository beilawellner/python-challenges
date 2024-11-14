class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)

        while l < r:
            k = (l + r) // 2

            products = 0
            for q in quantities:
                products += ceil(q / k)

            if products <= n:
                r = k
            else:
                l = k + 1
        return r