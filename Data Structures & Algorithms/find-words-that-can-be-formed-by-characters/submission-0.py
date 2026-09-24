from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        available = Counter(chars)
        total: int = 0
        for word in words:
            needed = Counter(word)
            if all(needed[ch] <= available[ch] for ch in needed):
                total += len(word)
        return total