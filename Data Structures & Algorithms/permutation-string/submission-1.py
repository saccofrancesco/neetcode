from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size: int = len(s1)
        if window_size > len(s2):
            return False
        target_count: int = Counter(s1)
        window_count: int = Counter(s2[:window_size])
        if window_count == target_count:
            return True
        for right in range(window_size, len(s2)):
            entering_char: str = s2[right]
            leaving_char: str = s2[right - window_size]
            window_count[entering_char] += 1
            window_count[leaving_char] -= 1
            if window_count[leaving_char] == 0:
                del window_count[leaving_char]
            if window_count == target_count:
                return True
        return False