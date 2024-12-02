class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        start = 0
        res = 0

        for c in s:
            if c == '(':
                start += 1
            elif c == ')':
                if start > 0:
                    start -= 1
                else:
                    res += 1

        return res + start
