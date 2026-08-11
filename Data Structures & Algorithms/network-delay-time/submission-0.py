import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, time in times:
            graph[u].append((v, time))

        # (distance from k, node)
        min_heap = [(0, k)]
        dist = {}

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            # We already found the shortest path to this node.
            if node in dist:
                continue

            dist[node] = current_time

            for neighbor, travel_time in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(
                        min_heap,
                        (current_time + travel_time, neighbor)
                    )

        if len(dist) != n:
            return -1

        return max(dist.values())