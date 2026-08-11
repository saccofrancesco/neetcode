import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # (minimum required time, row, col)
        min_heap = [(grid[0][0], 0, 0)]

        visited = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while min_heap:
            time, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and (nr, nc) not in visited
                ):
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(
                        min_heap,
                        (new_time, nr, nc)
                    )