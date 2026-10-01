class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n: int = len(nums)
        for x in range(n + 1):
            count: int = 0
            for num in nums:
                if num >= x:
                    count += 1
            if count == x:
                return x
        return -1