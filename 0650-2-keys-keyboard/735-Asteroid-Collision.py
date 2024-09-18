class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                # Calculate the difference to determine if the top of the stack survives
                diff = stack[-1] + a
                
                # If the top of the stack is larger, the current asteroid (a) is destroyed
                if diff > 0:
                    a = 0
                # If both are equal, both are destroyed
                elif diff == 0:
                    stack.pop()
                    a = 0
                # If the current asteroid is larger, the top of the stack is destroyed
                else:
                    stack.pop()
            
            # If a hasn't been destroyed, add it to the stack
            if a != 0:
                stack.append(a)
                    
        return stack
