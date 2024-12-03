'''
heights = [4,2,3,1]
taller = 0
'''
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = [len(heights) - 1]
        tallest = heights[-1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > tallest:
                res.append(i)
                tallest = heights[i]

        res.reverse()
        return res
