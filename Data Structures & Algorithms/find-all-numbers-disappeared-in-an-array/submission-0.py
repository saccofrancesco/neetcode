class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            i: int = abs(num) - 1
            nums[i] = -abs(nums[i])
        return [i + 1 for i, num in enumerate(nums) if num > 0]