class FirstUnique:

    def __init__(self, nums: List[int]):
        self.notuniques = set()
        self.uniques = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        for key in self.uniques:
            return key
        return -1

    def add(self, value: int) -> None:
        if value in self.notuniques:
            return
        if value in self.uniques:
            del self.uniques[value]
            self.notuniques.add(value)
        else:
            self.uniques[value] = None

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)