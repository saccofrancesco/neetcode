class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j: int = 0
        for char in s:
            if j < len(t) and char == t[j]:
                j += 1
        return len(t) - j