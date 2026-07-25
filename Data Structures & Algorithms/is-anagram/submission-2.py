class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts: List[int] = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1
        for char in t:
            index: int = ord(char) - 97
            counts[index] -= 1
            if counts[index] < 0:
                return False
        return True