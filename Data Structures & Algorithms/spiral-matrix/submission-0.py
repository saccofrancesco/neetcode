class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result: List[int] = list()
        top: int = 0
        bottom: int = len(matrix) - 1
        left: int = 0
        right: int = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result