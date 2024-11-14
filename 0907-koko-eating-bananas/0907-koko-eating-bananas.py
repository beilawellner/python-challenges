class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            k = (l + r) // 2
            hour_spent = 0

            for pile in piles:
                hour_spent += math.ceil(pile / k)

            if hour_spent <= h:
                r = k
            else:
                l = k + 1
        return r
