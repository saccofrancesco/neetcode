class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result: List[List[int]] = []
        def backtrack(start: int, remaining: int, current: List[int]) -> None:
            if remaining == 0:
                result.append(current.copy())
                return
            for i in range(start, len(nums)):
                value: int = nums[i]
                if value > remaining:
                    break
                current.append(value)
                backtrack(i, remaining - value, current)
                current.pop()

        backtrack(0, target, [])
        return result