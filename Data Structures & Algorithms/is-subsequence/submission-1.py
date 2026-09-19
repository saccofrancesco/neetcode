class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for char in t:
            if index == len(s):
                return True
            if char == s[index]:
                index += 1
        return index == len(s)