class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            prev: Tuple[int, int] = intervals[i - 1]
            curr: Tuple[int, int] = intervals[i]
            if curr.start < prev.end:
                return False
        return True