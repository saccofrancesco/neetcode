import heapq

class Solution:
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        # effort[r][c] = minimum effort needed to reach (r, c)
        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0

        # (effort, row, col)
        min_heap = [(0, 0, 0)]

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while min_heap:
            current_effort, row, col = heapq.heappop(min_heap)

            # Outdated heap entry
            if current_effort > effort[row][col]:
                continue

            # Destination reached
            if row == rows - 1 and col == cols - 1:
                return current_effort

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                ):
                    difference = abs(
                        heights[row][col] -
                        heights[new_row][new_col]
                    )

                    new_effort = max(
                        current_effort,
                        difference
                    )

                    if new_effort < effort[new_row][new_col]:
                        effort[new_row][new_col] = new_effort
                        heapq.heappush(
                            min_heap,
                            (new_effort, new_row, new_col)
                        )

        return 0