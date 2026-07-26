class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def squaredDistance(point: List[int]) -> int:
            x, y = point
            return x * x + y * y
        points.sort(key=squaredDistance)
        return points[:k]