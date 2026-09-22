class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        current = best = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += nums[i]
            else:
                current = nums[i]
            best = max(best, current)
        return best