class CustomStack:

    def __init__(self, maxSize: int):
        self._stack = []
        self._inc_stack = []
        self._max_size = maxSize

    def push(self, x: int) -> None:
        if len(self._stack) < self._max_size:
            self._stack.append(x)
            self._inc_stack.append(0)

    def pop(self) -> int:
        if not self._stack:
            return -1

        if len(self._inc_stack) > 1:
            self._inc_stack[-2] += self._inc_stack[-1] 
        
        return self._stack.pop() + self._inc_stack.pop()

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self._stack))
        if k > 0:
            self._inc_stack[k-1] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)