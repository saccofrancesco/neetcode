class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left: int = 0
        total: int = 0
        minLen: float = float("inf")
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                minLen = min(minLen, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if minLen == float("inf") else minLen