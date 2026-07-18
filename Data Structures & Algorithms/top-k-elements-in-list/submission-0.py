class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMapping: dict[int, int] = dict()
        for n in nums:
            if n in frequencyMapping:
                frequencyMapping[n] += 1
            else:
                frequencyMapping[n] = 1
        integerFrequencyList: list[tuple[int, int]] = list()
        for k, v in frequencyMapping.items():
            integerFrequency.append((k, v))
        integerFrequency.sort()
        result: list[int] = list()
        while len(result) < k:
            result.append(integerFrequency.pop()[0])
        return result