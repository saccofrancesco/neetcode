class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n: int = len(matrix)
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row],
                    matrix[row][col]
                )
        for row in matrix:
            row.reverse()