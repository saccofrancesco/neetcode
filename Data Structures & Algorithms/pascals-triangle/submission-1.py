class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle: list[list[int]] = list()
        for i in range(numRows):
            row: list[int] = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle