class Solution:
    def canJump(self, nums: List[int]) -> bool:
        finalIndex: int = len(nums) - 1
        currentIndex: int = 0
        while True:
            if currentIndex >= finalIndex:
                return True
            jumpAmount: int = nums[currentIndex]
            if jumpAmount == 0:
                return False
            currentIndex += jumpAmount