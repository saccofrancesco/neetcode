class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total: int = sum(nums)
        if total % 2 != 0:
            return False
        target: int = total // 2

        dp: List[bool] = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for current_sum in range(target, num - 1, -1):
                dp[current_sum] = (
                    dp[current_sum] or dp[current_sum - num]
                )
        return dp[target]