class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        balloons: list[int] = [1] + nums + [1]
        n: int = len(balloons)
        dp: list[list[int]] = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(n - length):
                right: int = left + length
                for i in range(left + 1, right):
                    coins: int = (
                        dp[left][i]
                        + balloons[left] * balloons[i] * balloons[right]
                        + dp[i][right]
                    )
                    dp[left][right] = max(dp[left][right], coins)
        return dp[0][n - 1]