class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []
        def backtrack(current: list[str], opened: int, closed: int) -> None:
            if len(current) == 2 * n:
                result.append("".join(current))
                return
            if opened < n:
                current.append("(")
                backtrack(current, opened + 1, closed)
                current.pop()
            if closed < opened:
                current.append(")")
                backtrack(current, opened, closed + 1)
                current.pop()
        backtrack([], 0, 0)
        return result