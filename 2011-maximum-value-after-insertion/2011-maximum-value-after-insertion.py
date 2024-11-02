class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            return '-' + self.minimize(n[1:], x)
        return self.maximize(n, x)

    def maximize(self, n, x):
        i = 0
        while i < len(n) and int(n[i]) >= x:
            i += 1
        return n[:i] + str(x) + n[i:]

    def minimize(self, n, x):
        i = 0
        while i < len(n) and int(n[i]) <= x:
            i += 1
        return n[:i] + str(x) + n[i:]
