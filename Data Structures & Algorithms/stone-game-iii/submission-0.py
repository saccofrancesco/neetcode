from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n: int = len(stoneValue)
        dp: List[int] = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            best: float = float("-inf")
            take_sum: int = 0
            for take in range(1, 4):
                if i + take > n:
                    break
                take_sum += stoneValue[i + take - 1]
                best: int / float = max(
                    best,
                    take_sum - dp[i + take]
                )
            dp[i] = best
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"