class Solution:
    def check(self, nums: list[int]) -> bool:
        drops: int = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                drops += 1
        return drops <= 1