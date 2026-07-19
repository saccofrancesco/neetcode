class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sequenceListMapping: dict[int, list[int]] = dict()
        currentKey: int = 0
        for n in sorted(nums):
            if not sequenceListMapping:
                sequenceListMapping[currentKey] = [n]
            else:
                if n == sequenceListMapping[currentKey][-1] + 1:
                    sequenceListMapping[currentKey].append(n)
                else:
                    currentKey += 1
                    sequenceListMapping[currentKey] = [n]
        return len(max(sequenceListMapping.values(), key=lambda x: len(x))) + 1