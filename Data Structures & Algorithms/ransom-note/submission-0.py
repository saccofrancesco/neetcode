from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = Counter(magazine)
        for ch in ransomNote:
            if available[ch] == 0:
                return False
            available[ch] -= 1
        return True