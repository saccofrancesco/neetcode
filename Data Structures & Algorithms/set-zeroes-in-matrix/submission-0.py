class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        first_row_zero: bool = any(matrix[0][col] == 0 for col in range(cols))
        first_col_zero: bool = any(matrix[row][0] == 0 for row in range(rows))
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0