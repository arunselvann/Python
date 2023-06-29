from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        row_zero = 1
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = 0

        for r in range(1, rows):
            for c in range(1, columns):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        if row_zero == 0:
            for c in range(columns):
                matrix[0][c] = 0


s = Solution()
m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
s.setZeroes(m)
print(m)
