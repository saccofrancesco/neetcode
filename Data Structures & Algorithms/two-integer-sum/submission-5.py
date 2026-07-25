class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            previous = seen.get(target - num)
            if previous is not None:
                return [previous, i]
            seen[num] = i