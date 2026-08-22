class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product: int = nums[0]
        min_product: int = nums[0]
        result: int = nums[0]
        for num in nums[1:]:
            prev_max: int = max_product
            prev_min: int = min_product

            max_product: int = max(
                num,
                num * prev_max,
                num * prev_min
            )
            min_product: int = min(
                num,
                num * prev_max,
                num * prev_min
            )
            result = max(result, max_product)
        return result