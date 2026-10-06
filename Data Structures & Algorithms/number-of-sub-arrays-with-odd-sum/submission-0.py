from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even = 1  # empty prefix has sum 0
        odd = 0
        prefix = 0
        ans = 0
        for num in arr:
            prefix += num
            if prefix % 2 == 0:
                # Need a previous odd prefix
                ans += odd
                even += 1
            else:
                # Need a previous even prefix
                ans += even
                odd += 1
        return ans % MOD