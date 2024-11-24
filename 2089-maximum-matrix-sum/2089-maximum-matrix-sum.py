class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_val = abs(matrix[0][0])
        count_neg = 0
        summation = 0
        for row in matrix:
            for n in row:
                if n < 0:
                    count_neg += 1
                min_val = min(min_val, abs(n))
                summation += abs(n)
        return summation if count_neg % 2 == 0 else (summation - 2 * min_val)
