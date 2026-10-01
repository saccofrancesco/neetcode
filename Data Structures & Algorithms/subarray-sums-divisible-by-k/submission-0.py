from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix: int = 0
        result: int = 0
        for num in nums:
            prefix += num
            remainder = prefix % k
            result += count[remainder]
            count[remainder] += 1
        return result