class Solution:
    def binaryExp(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        res = self.binaryExp(x * x, n // 2)
        return res if n % 2 == 0 else x * res

    def myPow(self, x: float, n: int) -> float:
        res = self.binaryExp(x, abs(n))
        return res if n > 0 else 1.0 / res
