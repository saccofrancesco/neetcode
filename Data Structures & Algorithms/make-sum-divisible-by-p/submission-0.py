from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p

        # Already divisible by p
        if target == 0:
            return 0

        # remainder -> latest index where that prefix remainder occurred
        last_seen = {0: -1}

        prefix = 0
        ans = len(nums)

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            needed = (prefix - target) % p

            if needed in last_seen:
                ans = min(ans, i - last_seen[needed])

            # Keep latest occurrence to minimize subarray length
            last_seen[prefix] = i

        # Removing the entire array is not allowed
        return ans if ans < len(nums) else -1