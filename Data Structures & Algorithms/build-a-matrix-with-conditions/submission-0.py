from typing import List
from collections import deque


class Solution:
    def buildMatrix(
        self,
        k: int,
        rowConditions: List[List[int]],
        colConditions: List[List[int]]
    ) -> List[List[int]]:

        def topological_sort(conditions):
            graph = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)

            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1

            queue = deque()

            for node in range(1, k + 1):
                if indegree[node] == 0:
                    queue.append(node)

            order = []

            while queue:
                node = queue.popleft()
                order.append(node)

                for neighbor in graph[node]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            # Cycle exists
            if len(order) != k:
                return []

            return order

        row_order = topological_sort(rowConditions)
        col_order = topological_sort(colConditions)

        if not row_order or not col_order:
            return []

        # Map each number to its row and column.
        row_position = [0] * (k + 1)
        col_position = [0] * (k + 1)

        for row, value in enumerate(row_order):
            row_position[value] = row

        for col, value in enumerate(col_order):
            col_position[value] = col

        matrix = [[0] * k for _ in range(k)]

        for value in range(1, k + 1):
            row = row_position[value]
            col = col_position[value]

            matrix[row][col] = value

        return matrix