class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_hash_table: dict[int, int] = {}
        for i, n in enumerate(nums):
            needed: int = target - nums[i]
            if needed in seen_hash_table:
                index: int = seen_hash_table[needed]
                if i < index:
                    return [i, index]
                else:
                    return [index, i]
            else:
                seen_hash_table[n] = i