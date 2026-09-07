from typing import List


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[List[int]]:

        # Keep each edge's original index.
        indexed_edges = [
            (weight, u, v, i)
            for i, (u, v, weight) in enumerate(edges)
        ]

        indexed_edges.sort()

        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, a, b):
                root_a = self.find(a)
                root_b = self.find(b)

                if root_a == root_b:
                    return False

                if self.rank[root_a] < self.rank[root_b]:
                    root_a, root_b = root_b, root_a

                self.parent[root_b] = root_a

                if self.rank[root_a] == self.rank[root_b]:
                    self.rank[root_a] += 1

                return True

        def kruskal(skip=None, force=None):
            """
            skip  = original index of an edge we cannot use
            force = original index of an edge we must use
            """
            dsu = DSU(n)
            total_weight = 0
            edges_used = 0

            # Force one edge into the MST first.
            if force is not None:
                u, v, weight = edges[force]

                if dsu.union(u, v):
                    total_weight += weight
                    edges_used += 1

            # Normal Kruskal.
            for weight, u, v, idx in indexed_edges:
                if idx == skip or idx == force:
                    continue

                if dsu.union(u, v):
                    total_weight += weight
                    edges_used += 1

                    if edges_used == n - 1:
                        break

            # Could not create a spanning tree.
            if edges_used != n - 1:
                return float("inf")

            return total_weight

        # Weight of a normal MST.
        base_weight = kruskal()

        critical = []
        pseudo_critical = []

        for i in range(len(edges)):
            # Test 1: remove edge i.
            without_edge = kruskal(skip=i)

            if without_edge > base_weight:
                critical.append(i)
                continue

            # Test 2: force edge i.
            with_edge = kruskal(force=i)

            if with_edge == base_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]