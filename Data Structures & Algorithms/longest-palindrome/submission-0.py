from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length: int = 0
        has_odd: bool = False
        for freq in count.values():
            length += (freq // 2) * 2
            if freq % 2 == 1:
                has_odd = True
        if has_odd:
            length += 1
        return length