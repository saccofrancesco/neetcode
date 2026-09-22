class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n: int = len(grid)
        N: int = n * n
        actual_sum: int = 0
        actual_sq_sum: int = 0
        for row in grid:
            for x in row:
                actual_sum += x
                actual_sq_sum += x * x
        expected_sum: int = N * (N + 1) // 2
        expected_sq_sum: int = N * (N + 1) * (2 * N + 1) // 6
        diff: int = actual_sum - expected_sum
        sq_diff: int = actual_sq_sum - expected_sq_sum
        total: int = sq_diff // diff
        repeated: int = (diff + total) // 2
        missing: int = total - repeated
        return [repeated, missing]