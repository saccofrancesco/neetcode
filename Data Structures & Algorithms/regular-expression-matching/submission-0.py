class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo: dict = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            # Pattern finished
            if j == len(p):
                return i == len(s)
            first_match: bool = (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            )
            # If next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == "*":
                memo[(i, j)] = (
                    dfs(i, j + 2)          # use '*' zero times
                    or
                    (first_match and dfs(i + 1, j))  # use '*' one or more times
                )
            else:
                memo[(i, j)] = (
                    first_match
                    and dfs(i + 1, j + 1)
                )
            return memo[(i, j)]
        return dfs(0, 0)