from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        count: list [int] = [0] * (n + 1)
        for num in nums:
            count[num] += 1
        duplicate: int = -1
        missing: int = -1
        for num in range(1, n + 1):
            if count[num] == 2:
                duplicate = num
            elif count[num] == 0:
                missing = num
        return [duplicate, missing]