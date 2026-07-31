class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area: int = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 1:
                    continue
                area: int = 0
                stack: List[Tuple[int, int]] = [(row, col)]
                grid[row][col] = 0
                while stack:
                    current_row, current_col = stack.pop()
                    area += 1
                    for next_row, next_col in (
                        (current_row + 1, current_col),
                        (current_row - 1, current_col),
                        (current_row, current_col + 1),
                        (current_row, current_col - 1),
                    ):
                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid[next_row][next_col] == 1
                        ):
                            grid[next_row][next_col] = 0
                            stack.append((next_row, next_col))
                max_area: int = max(max_area, area)
        return max_area
