from functools import cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from piles[i] to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @cache
        def dp(i: int, M: int) -> int:
            # If we can take every remaining pile, do it
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            for X in range(1, 2 * M + 1):
                opponent = dp(i + X, max(M, X))

                # Total remaining stones - opponent's best score
                current = suffix[i] - opponent

                best = max(best, current)

            return best

        return dp(0, 1)