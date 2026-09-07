class Solution:
    def integerBreak(self, n: int) -> int:
        dp: List[int] = [0] * (n + 1)
        dp[1] = 1
        for total in range(2, n + 1):
            for first in range(1, total):
                second: int = total - first
                dp[total] = max(
                    dp[total],
                    first * second,
                    first * dp[second]
                )
        return dp[n]