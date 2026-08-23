from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex: dict[str, int] = dict()
        for i, char in enumerate(s):
            lastIndex[char] = i
        result: List[int] = list()
        start: int = 0
        end: int = 0
        for i, char in enumerate(s):
            end: int = max(end, lastIndex[char])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result