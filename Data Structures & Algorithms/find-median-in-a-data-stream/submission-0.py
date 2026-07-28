from bisect import insort

class MedianFinder:

    def __init__(self):
        self.values: List[int] = []
        self.length: int = 0

    def addNum(self, num: int) -> None:
        insort(self.values, num)
        self.length += 1

    def findMedian(self) -> float:
        m: int = self.length // 2
        if self.length % 2 == 0:
            return (self.values[m - 1] + self.values[m]) / 2
        else:
            return self.values[m]