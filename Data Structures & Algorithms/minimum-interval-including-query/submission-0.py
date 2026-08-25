import heapq


class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()

        # Store (query_value, original_index)
        sorted_queries = sorted(
            (query, i) for i, query in enumerate(queries)
        )

        result = [-1] * len(queries)

        # Heap stores: (interval_length, right_endpoint)
        heap = []

        i = 0

        for query, original_index in sorted_queries:

            # Add every interval whose left endpoint <= query
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                length = right - left + 1

                heapq.heappush(heap, (length, right))
                i += 1

            # Remove intervals that end before the query
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            # Smallest valid interval is at the top
            if heap:
                result[original_index] = heap[0][0]

        return result