class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result: List[List[int]]= [intervals[0]]
        for start, end in intervals[1:]:
            last_end: int = result[-1][1]
            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append([start, end])
        return result