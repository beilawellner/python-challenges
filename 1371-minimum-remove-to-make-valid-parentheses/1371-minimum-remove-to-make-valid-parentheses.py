'''
"lee(t(c)o)de)"
"lee"
""
"le((()e(t(c)o)de"
"((((("
")))))"
open_stack = [i]
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indices_to_remove = []
        res = ""

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    indices_to_remove.append(i)

        for i in range(len(s)):
            if i not in stack + indices_to_remove:
                res += s[i]

        return res