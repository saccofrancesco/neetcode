class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        result: List[int] = [1] * n
        prefix: int = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        suffix: int = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result