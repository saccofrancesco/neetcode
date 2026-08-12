class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(houses: List[int]) -> int:
            prev2: int = 0
            prev1: int = 0
            for money in houses:
                current: int = max(
                    prev1,
                    prev2 + money
                )
                prev2 = prev1
                prev1 = current
            return prev1
        return max(
            rob_line(nums[:-1]),
            rob_line(nums[1:])
        )