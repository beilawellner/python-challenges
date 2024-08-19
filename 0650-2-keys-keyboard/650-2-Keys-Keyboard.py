'''
n = 5
[0,1,1,]
'''
class Solution:
    def recursive_steps(self, cur_len, paste_len, n):
        if cur_len == n:
            return 0
        if cur_len > n:
            return 1000
        
        # copy+paste
        opt1 = 2 + self.recursive_steps(cur_len * 2, cur_len, n)
        # paste
        opt2 = 1 + self.recursive_steps(cur_len + paste_len, paste_len, n)

        return min(opt1, opt2)

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        return 1 + self.recursive_steps(1, 1, n)

        