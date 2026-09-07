from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2: int = 0
        prev1: int = 0
        for c in cost:
            current: int = c + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
        return min(prev1, prev2)