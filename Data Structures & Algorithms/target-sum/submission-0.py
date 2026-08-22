class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp: dict[int, int] = {0: 1}
        for num in nums:
            next_dp: dict[int, int] = {}
            for total, ways in dp.items():
                plus: int = total + num
                minus: int = total - num
                next_dp[plus] = next_dp.get(plus, 0) + ways
                next_dp[minus] = next_dp.get(minus, 0) + ways
            dp = next_dp
        return dp.get(target, 0)