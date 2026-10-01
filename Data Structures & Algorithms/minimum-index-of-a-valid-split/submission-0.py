from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n: int = len(nums)
        count = Counter(nums)
        dominant: int = max(count, key=count.get)
        total: int = count[dominant]
        left_count: int = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                left_count += 1
            left_size: int = i + 1
            right_size: int = n - left_size
            right_count: int = total - left_count
            if left_count * 2 > left_size and right_count * 2 > right_size:
                return i
        return -1