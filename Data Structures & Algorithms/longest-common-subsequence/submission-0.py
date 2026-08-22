class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n: int = len(text2)
        dp: List[int] = [0] * (n + 1)
        for i in range(1, len(text1) + 1):
            prev: int = 0
            for j in range(1, n + 1):
                temp: int = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp
        return dp[n]