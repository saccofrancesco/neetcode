class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        left: int = 0
        right: int = len(arr) - k
        while left < right:
            mid: int = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]