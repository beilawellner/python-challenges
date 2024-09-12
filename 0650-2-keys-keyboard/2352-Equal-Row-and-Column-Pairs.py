class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        res = 0

        for row in grid:
            d[tuple(row)] += 1
        
        for i in range(len(grid[0])):
            column = tuple([row[i] for row in grid])
            res += d[column]
            
        return res