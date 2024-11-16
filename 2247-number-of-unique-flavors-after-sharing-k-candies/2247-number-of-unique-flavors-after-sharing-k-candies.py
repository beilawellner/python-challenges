class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        counter = Counter(candies[k:])
        res = len(counter)

        for i in range(k, len(candies)):
            counter[candies[i - k]] += 1
            cur_candy = candies[i]
            counter[cur_candy] -= 1
            if counter[cur_candy] <= 0:
                counter.pop(cur_candy)
            res = max(res, len(counter))

        return res
