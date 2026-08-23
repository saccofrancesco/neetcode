class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximumSum: float = float("-inf")
        for i, num in enumerate(nums):
            total: float = 0
            for n in nums[i:]:
                total += n
            if total > maximumSum:
                maximumSum = total
        return maximumSum