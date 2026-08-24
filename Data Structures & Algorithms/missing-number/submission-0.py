class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        missing: int = len(nums)
        for i, num in enumerate(nums):
            missing ^= i
            missing ^= num
        return missing