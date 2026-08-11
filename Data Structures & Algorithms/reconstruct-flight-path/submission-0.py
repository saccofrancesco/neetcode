from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Reverse sorting lets us pop the lexicographically
        # smallest destination from the end in O(1).
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            # Add airport only after all outgoing tickets are used.
            itinerary.append(airport)

        dfs("JFK")

        # Hierholzer constructs the path backwards.
        return itinerary[::-1]