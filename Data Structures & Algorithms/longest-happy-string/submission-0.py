import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        result = []

        while heap:
            freq1, char1 = heapq.heappop(heap)

            # If using char1 would create aaa/bbb/ccc,
            # use the second most frequent character instead.
            if (
                len(result) >= 2
                and result[-1] == char1
                and result[-2] == char1
            ):
                if not heap:
                    break

                freq2, char2 = heapq.heappop(heap)

                result.append(char2)
                freq2 += 1

                if freq2 < 0:
                    heapq.heappush(heap, (freq2, char2))

                # char1 wasn't used, so put it back
                heapq.heappush(heap, (freq1, char1))

            else:
                result.append(char1)
                freq1 += 1

                if freq1 < 0:
                    heapq.heappush(heap, (freq1, char1))

        return "".join(result)