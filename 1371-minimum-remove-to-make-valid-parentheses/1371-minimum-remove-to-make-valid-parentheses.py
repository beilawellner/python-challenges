class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_cnt = 0
        res = []

        for c in s:
            if c == '(':
                open_cnt += 1
                res.append(c)
            elif c == ')' and open_cnt:
                open_cnt -= 1
                res.append(c)
            elif c != ')':
                res.append(c)

        filtered = []
        for c in reversed(res):
            if c == '(' and open_cnt:
                open_cnt -= 1
            else:
                filtered.append(c)

        return ''.join(reversed(filtered))