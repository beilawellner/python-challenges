class Solution:

    def __init__(self, w: List[int]):
        self.sum_list = []
        total = 0
        for weight in w:
            total += weight
            self.sum_list.append(total)

    def pickIndex(self) -> int:
        target = random.uniform(0, self.sum_list[-1])
        l, r = 0, len(self.sum_list)

        while l < r:
            m = (l + r) // 2
            if self.sum_list[m] < target:
                l = m + 1
            else:
                r = m
        return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()