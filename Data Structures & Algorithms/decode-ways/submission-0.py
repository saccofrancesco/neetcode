class Solution:
    def numDecodings(self, s: str) -> int:
        prev2: int = 1
        prev1: int = 0 if s[0] == "0" else 1
        for i in range(1, len(s)):
            current: int = 0
            # Decode current digit by itself
            if s[i] != "0":
                current += prev1
            # Decode previous + current digit together
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                current += prev2
            prev2 = prev1
            prev1 = current
        return prev1