class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index: int = 0
        for char in t:
            if char == s[index]:
                index += 1
        return index == len(s) - 1