class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        total: int = sum(stones)
        target: int = total // 2
        dp: list[bool] = [False] * (target + 1)
        dp[0] = True
        for stone in stones:
            for s in range(target, stone - 1, -1):
                dp[s] = dp[s] or dp[s - stone]
        for s in range(target, -1, -1):
            if dp[s]:
                return total - 2 * s