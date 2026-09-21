class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current: int = 0
        maximum: int = 0
        for num in nums:
            if num == 1:
                current += 1
                maximum = max(maximum, current)
            else:
                current = 0
        return maximum