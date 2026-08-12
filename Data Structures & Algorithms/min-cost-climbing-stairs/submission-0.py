class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2: int = 0
        prev1: int = 0
        for i in range(2, len(cost) + 1):
            current: int = min(
                prev1 + cost[i - 1],
                prev2 + cost[i - 2]
            )
            prev2 = prev1
            prev1 = current
        return prev1