class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        min_val = abs(matrix[0][0])
        count_neg = 0
        summation = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] < 0:
                    count_neg += 1
                abs_val = abs(matrix[r][c])
                min_val = min(min_val, abs_val)
                summation += abs_val
        return summation if count_neg % 2 == 0 else (summation - 2 * min_val)
