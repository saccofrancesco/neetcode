# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid: int = left + (right - left) // 2
            result: int = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            else:
                right = mid - 1