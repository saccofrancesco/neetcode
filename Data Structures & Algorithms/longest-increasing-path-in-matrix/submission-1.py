class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows: int = len(matrix)
        cols: int = len(matrix[0])
        dp: list[list[int]] = [[0] * cols for _ in range(rows)]
        directions: list[tuple[int, int]] = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        def dfs(r, c):
            if dp[r][c] != 0:
                return dp[r][c]
            longest: int = 1
            for dr, dc in directions:
                nr: int = r + dr
                nc: int = c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and matrix[nr][nc] > matrix[r][c]
                ):
                    longest: int = max(longest, 1 + dfs(nr, nc))
            dp[r][c] = longest
            return longest
        answer: int = 0
        for r in range(rows):
            for c in range(cols):
                answer = max(answer, dfs(r, c))
        return answer