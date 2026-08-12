class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2: int = 0
        prev1: int = 0
        for money in nums:
            current = max(
                prev1,
                prev2 + money
            )
            prev2 = prev1
            prev1 = current
        return prev1