class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])

        res = [['.'] * rows for _ in range(cols)]

        for r in range(rows):
            nxt_free = cols - 1
            for c in range(cols - 1, -1, -1):
                if box[r][c] == '*':
                    res[c][rows - r - 1] = '*'
                    nxt_free = c - 1
                elif box[r][c] == '#':
                    res[nxt_free][rows - r - 1] = '#'
                    nxt_free -= 1
        return res

