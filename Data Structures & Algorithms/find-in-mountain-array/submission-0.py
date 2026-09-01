class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. Find the peak
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        # 2. Binary search on increasing part
        left = 0
        right = peak

        while left <= right:
            mid = left + (right - left) // 2
            value = mountainArr.get(mid)

            if value == target:
                return mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        # 3. Binary search on decreasing part
        left = peak + 1
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            value = mountainArr.get(mid)

            if value == target:
                return mid
            elif value < target:
                # Array is decreasing, so smaller values are on the right
                right = mid - 1
            else:
                left = mid + 1

        return -1