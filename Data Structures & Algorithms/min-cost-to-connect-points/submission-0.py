from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_dist = [float("inf")] * n
        min_dist[0] = 0

        visited = [False] * n
        total_cost = 0

        for _ in range(n):
            # Find the unvisited point with the cheapest
            # connection to the current MST.
            curr = -1

            for i in range(n):
                if not visited[i] and (
                    curr == -1 or min_dist[i] < min_dist[curr]
                ):
                    curr = i

            visited[curr] = True
            total_cost += min_dist[curr]

            x1, y1 = points[curr]

            # Update connection costs for remaining points.
            for nxt in range(n):
                if not visited[nxt]:
                    x2, y2 = points[nxt]

                    distance = abs(x1 - x2) + abs(y1 - y2)

                    min_dist[nxt] = min(
                        min_dist[nxt],
                        distance
                    )

        return total_cost