class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        operator = '+'  # Default operator before the first number
        
        # Remove spaces for safety
        s = s.replace(' ', '')
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            
            if c in "+-*/" or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                elif operator == '/':
                    last_num = stack.pop()
                    if last_num < 0:
                        stack.append(-(-last_num // num)) 
                    else:
                        stack.append(last_num // num)
                
                num = 0
                operator = c
        
        return sum(stack)