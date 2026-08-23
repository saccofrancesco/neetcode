class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps: int = 0
        currentEnd: int = 0
        maxReach: int = 0
        for i in range(len(nums) - 1):
            maxReach = max(maxReach, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = maxReach
        return jumps