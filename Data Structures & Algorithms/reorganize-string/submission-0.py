import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        # Max heap: (-frequency, character)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        result = []

        # Previous character that we cannot use immediately again
        prev_freq = 0
        prev_char = ""

        while heap:
            freq, char = heapq.heappop(heap)

            result.append(char)

            # Put the previous character back into the heap
            # now that we've placed a different character.
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            # We used one occurrence of char
            freq += 1

            prev_freq = freq
            prev_char = char

        # If the previous character still has occurrences left,
        # we couldn't place all characters.
        if prev_freq < 0:
            return ""

        return "".join(result)