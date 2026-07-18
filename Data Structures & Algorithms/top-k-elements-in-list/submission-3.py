class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency: dict[int, int] = dict()
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        numFreqList: list[tuple[int, int]] = list()
        for n, f in frequency.items():
            numFreqList.append((n, f))
        numFreqList.sort(key=lambda x: x[1])
        result: list[int] = list()
        while len(result) < k:
            result.append(numFreqList.pop()[0])
        return result