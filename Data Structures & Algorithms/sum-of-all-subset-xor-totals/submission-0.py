class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        total_or: int = 0
        for num in nums:
            total_or |= num
        return total_or * (1 << (len(nums) - 1))