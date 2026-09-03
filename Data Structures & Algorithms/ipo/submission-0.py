import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        projects = sorted(zip(capital, profits))

        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):

            # Add every project we can currently afford
            while i < n and projects[i][0] <= w:
                required_capital, profit = projects[i]

                # Python has a min heap, so use negative profit
                heapq.heappush(max_heap, -profit)
                i += 1

            # No project can currently be started
            if not max_heap:
                break

            # Pick the available project with maximum profit
            w += -heapq.heappop(max_heap)

        return w