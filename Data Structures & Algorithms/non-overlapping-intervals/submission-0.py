class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals: int = 0
        last_end: List[List[int]] = intervals[0][1]
        for start, end in intervals[1:]:
            if start < last_end:
                removals += 1
            else:
                last_end = end
        return removals