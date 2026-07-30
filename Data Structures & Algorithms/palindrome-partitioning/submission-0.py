class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n: int = len(s)
        result: List[List[str]] = []
        partition: List[str] = []
        palindrome: List[bool] = [[False] * n for _ in range(n)]
        for start in range(n - 1, -1, -1):
            for end in range(start, n):
                if s[start] == s[end] and (
                    end - start <= 2 or palindrome[start + 1][end - 1]
                ):
                    palindrome[start][end] = True
        def backtrack(start: int) -> None:
            if start == n:
                result.append(partition.copy())
                return
            for end in range(start, n):
                if not palindrome[start][end]:
                    continue
                partition.append(s[start : end + 1])
                backtrack(end + 1)
                partition.pop()
        backtrack(0)
        return result