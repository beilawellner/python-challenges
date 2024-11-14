class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                cur_str = ''
                while stack[-1] != '[':
                    cur_str = stack.pop() + cur_str
                stack.pop()

                dup = ''
                while stack and stack[-1].isdigit():
                    dup = stack.pop() + dup
                stack.append(int(dup) * cur_str)
        return "".join(stack)
