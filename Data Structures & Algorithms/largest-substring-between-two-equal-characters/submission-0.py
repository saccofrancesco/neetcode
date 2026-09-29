class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first: dict[str, int] = {}
        result: int = -1
        for i, char in enumerate(s):
            if char in first:
                result = max(result, i - first[char] - 1)
            else:
                first[char] = i
        return result