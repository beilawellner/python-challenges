class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        cur = 1
        while len(res) < n:
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10  # Move to the next level (e.g., 1 -> 10).
            else:
                while cur >= n or cur % 10 == 9:
                    cur //= 10  # Go back to the parent level when necessary.
                cur += 1  # Move to the next sibling.
        return res
