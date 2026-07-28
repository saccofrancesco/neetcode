class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        def backtrack(start: int, current: List[int]) -> None:
            result.append(current.copy())
            for index in range(start, len(nums)):
                current.append(nums[index])
                backtrack(index + 1, current)
                current.pop()
        backtrack(0, [])
        return result