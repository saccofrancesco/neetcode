from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        directions = (
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        )
        while queue:
            row, col = queue.popleft()
            for row_change, col_change in directions:
                next_row = row + row_change
                next_col = col + col_change
                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col] == 2147483647
                ):
                    grid[next_row][next_col] = grid[row][col] + 1
                    queue.append((next_row, next_col))
