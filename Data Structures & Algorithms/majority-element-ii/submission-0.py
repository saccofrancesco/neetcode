class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        countMap: dict[int, int] = dict()
        minimum: float = len(nums) / 3
        result: List[int] = list()
        for n in nums:
            if n not in countMap:
                count: int = nums.count(n)
                countMap[n] = count
                if count > minimum:
                    result.append(n)
        return result