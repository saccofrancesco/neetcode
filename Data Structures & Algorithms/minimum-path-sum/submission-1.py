class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])
        dp: list[list[int]] = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for r in range(1, rows):
            dp[r][0] = dp[r - 1][0] + grid[r][0]
        for c in range(1, cols):
            dp[0][c] = dp[0][c - 1] + grid[0][c]
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = grid[r][c] + min(
                    dp[r - 1][c],   # from above
                    dp[r][c - 1]    # from left
                )
        return dp[rows - 1][cols - 1]