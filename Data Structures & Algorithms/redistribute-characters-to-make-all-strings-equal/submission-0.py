from collections import Counter
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = Counter()
        for word in words:
            count.update(word)
        n: int = len(words)
        for freq in count.values():
            if freq % n != 0:
                return False
        return True