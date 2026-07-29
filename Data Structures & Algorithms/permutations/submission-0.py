class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        def backtrack(index: int) -> None:
            if index == len(nums):
                result.append(nums.copy())
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        backtrack(0)
        return result