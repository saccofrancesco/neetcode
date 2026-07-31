from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        def bfs(queue: deque) -> set[tuple[int, int]]:
            reachable = set(queue)
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
                        and (next_row, next_col) not in reachable
                        and heights[next_row][next_col] >= heights[row][col]
                    ):
                        reachable.add((next_row, next_col))
                        queue.append((next_row, next_col))
            return reachable
        pacific_queue = deque()
        atlantic_queue = deque()
        for row in range(rows):
            pacific_queue.append((row, 0))
            atlantic_queue.append((row, cols - 1))
        for col in range(cols):
            pacific_queue.append((0, col))
            atlantic_queue.append((rows - 1, col))
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        return [
            [row, col]
            for row, col in pacific_reachable & atlantic_reachable
        ]
