from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq = Counter(nums)
        pairs: int = 0
        for count in freq.values():
            pairs += count * (count - 1) // 2
        return pairs