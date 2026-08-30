class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums[:-2]):
            if n == target:
                return i
            if n < target < nums[i + 1]:
                return i + 1
        return len(nums)