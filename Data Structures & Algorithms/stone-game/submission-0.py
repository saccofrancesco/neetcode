class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        n: int = len(piles)
        dp: list[list[int]] = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right: int = left + length - 1
                take_left: int = piles[left] - dp[left + 1][right]
                take_right: int = piles[right] - dp[left][right - 1]
                dp[left][right] = max(take_left, take_right)
        return dp[0][n - 1] > 0