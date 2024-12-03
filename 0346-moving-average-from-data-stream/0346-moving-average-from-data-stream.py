class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.total -= self.queue.popleft()
        self.total += val
        self.queue.append(val)
        
        return self.total / min(self.size, len(self.queue))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)