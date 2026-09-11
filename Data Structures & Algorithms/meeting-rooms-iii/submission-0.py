import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        available: list[int] = list(range(n))
        heapq.heapify(available)
        used = []
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free every room available by this meeting's start time
            while used and used[0][0] <= start:
                end_time, room = heapq.heappop(used)
                heapq.heappush(available, room)

            if available:
                # Use the lowest-numbered available room
                room = heapq.heappop(available)
                heapq.heappush(used, (end, room))

            else:
                # No room available:
                # delay until the earliest room becomes free
                end_time, room = heapq.heappop(used)

                new_end = end_time + duration

                heapq.heappush(used, (new_end, room))

            count[room] += 1

        return count.index(max(count))