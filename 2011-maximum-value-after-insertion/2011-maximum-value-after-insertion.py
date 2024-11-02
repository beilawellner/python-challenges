'''
99999
66666
-2345
'''
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        positive = True if n[0] != '-' else False
        i = 0 if positive else 1
        if positive:
            while i < len(n) and int(n[i]) >= x:
                i += 1
        else:
            while i < len(n) and int(n[i]) <= x:
                i += 1
        n = n[:i] + str(x) + n[i:]

        return n