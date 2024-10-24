class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        legal_moves = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]

        def _is_valid_move(to_row, to_col):
            return (
                0 <= to_row < m
                and 0 <= to_col < n
                and res[to_row][to_col] == 0
            )

        def _solve(r, c, moves):
            if moves == m * n:
                return True

            for move_r, move_c in legal_moves:
                new_row, new_col = r + move_r, c + move_c
                if _is_valid_move(new_row, new_col):
                    res[new_row][new_col] = moves

                    if _solve(new_row, new_col, moves + 1):
                        return True

                    res[new_row][new_col] = 0

        res = [[0] * n for _ in range(m)]
        res[r][c] = -1

        _solve(r, c, 1)

        res[r][c] = 0

        return res
