class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m: int = len(word1)
        n: int = len(word2)
        dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]
        # Convert word1[:i] into ""
        # We must delete all i characters
        for i in range(m + 1):
            dp[i][0] = i
        # Convert "" into word2[:j]
        # We must insert all j characters
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert: int = dp[i][j - 1]
                    delete: int = dp[i - 1][j]
                    replace: int = dp[i - 1][j - 1]
                    dp[i][j] = 1 + min(insert, delete, replace)
        return dp[m][n]