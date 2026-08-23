class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximumSum: float = float("-inf")
        currentSum: float = 0
        for num in nums:
            currentSum: float = max(num, currentSum + num)
            maximumSum: float = max(maximumSum, currentSum)
        return maximumSum