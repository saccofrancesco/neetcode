class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m: int = len(s)
        n: int = len(t)
        dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]
        # Empty t can always be created in exactly one way:
        # choose nothing from s
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Don't use s[i - 1]
                dp[i][j] = dp[i - 1][j]
                # If characters match, we can also use s[i - 1]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[m][n]