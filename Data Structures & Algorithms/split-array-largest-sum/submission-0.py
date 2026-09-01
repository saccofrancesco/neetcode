class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        left: int = max(nums)
        right: int = sum(nums)
        def can_split(max_sum: int) -> bool:
            subarrays: int= 1
            current_sum: int = 0
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True
        while left < right:
            mid: int = left + (right - left) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left