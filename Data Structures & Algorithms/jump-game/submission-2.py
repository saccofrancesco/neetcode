class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach: int = 0
        for i, jumpAmount in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + jumpAmount)
        return True