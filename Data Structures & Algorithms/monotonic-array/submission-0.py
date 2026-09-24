class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing: bool = True
        decreasing: bool = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increasing = False
            if nums[i] > nums[i - 1]:
                decreasing = False
        return increasing or decreasing