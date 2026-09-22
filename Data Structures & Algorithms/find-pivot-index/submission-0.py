class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total: int = sum(nums)
        left: int = 0
        for i, num in enumerate(nums):
            right: int = total - left - num
            if left == right:
                return i
            left += num
        return -1