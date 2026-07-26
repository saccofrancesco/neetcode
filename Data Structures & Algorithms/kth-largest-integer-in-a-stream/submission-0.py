import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream: List[int] = nums
        self.stream.sort(reverse=True)
        self.ith: int = k

    def add(self, val: int) -> int:
        lo, hi = 0, len(self.stream)
        while lo < hi:
            mid: int = (lo + hi) // 2
            if self.stream[mid] > val:
                lo = mid + 1
            else:
                hi = mid
        self.stream.insert(lo, val)
        return self.stream[self.ith - 1]