import heapq

class Solution:
    def getOrder(self, tasks):
        # Add original index:
        # [enqueue_time, processing_time, index]
        tasks = [
            (enqueue, processing, i)
            for i, (enqueue, processing) in enumerate(tasks)
        ]

        # Sort by enqueue time
        tasks.sort()

        heap = []
        result = []

        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:

            # If CPU is idle, jump to the next task's enqueue time
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            # Add all tasks that are currently available
            while i < n and tasks[i][0] <= time:
                enqueue, processing, index = tasks[i]

                # heap orders by:
                # 1. processing time
                # 2. index
                heapq.heappush(heap, (processing, index))

                i += 1

            # Process the best available task
            processing, index = heapq.heappop(heap)

            result.append(index)
            time += processing

        return result