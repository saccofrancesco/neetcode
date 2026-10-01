class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        result = []
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]
        for num in sorted(count):
            result.extend([num] * count[num])
        return result