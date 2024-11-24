class Solution:
    def calculate(self, s: str) -> int:
        num, last_num, res = 0, 0, 0
        operator = '+'
                
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            
            if c in "+-*/" or i == len(s) - 1:
                if operator == '+':
                    res += last_num
                    last_num = num
                elif operator == '-':
                    res += last_num
                    last_num = -num
                elif operator == '*':
                    last_num *= num
                elif operator == '/':
                    if last_num < 0:
                        last_num = -(-last_num // num)
                    else:
                        last_num = last_num // num
                
                num = 0
                operator = c

        res += last_num        
        return res