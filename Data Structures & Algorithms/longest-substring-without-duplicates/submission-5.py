class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        streaks: dict[int, List[int]] = {
            0: []
        }
        current: int = 0
        for i, char in enumerate(s):
            for c in s[i + 1:]:
                if c not in streaks[current]:
                    streaks[current].append(c)
                else:
                    current += 1
                    streaks[current] = []
                    break
        return len(max(streaks.values(), key=lambda x: len(x)))