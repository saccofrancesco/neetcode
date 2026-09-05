class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n: int = len(s)
        dp: List[int] = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            for word in dictionary:
                if s.startswith(word, i):
                    dp[i] = min(dp[i], dp[i + len(word)])
        return dp[0]