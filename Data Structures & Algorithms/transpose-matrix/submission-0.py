class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        result: list[list[int]] = [[0] * rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                result[c][r] = matrix[r][c]
        return result