from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: list[int]) -> int:
        x, y = point
        squares = 0

        for (px, py), freq in self.points.items():
            if px == x or py == y:
                continue

            if abs(px - x) != abs(py - y):
                continue

            squares += (
                freq
                * self.points.get((px, y), 0)
                * self.points.get((x, py), 0)
            )

        return squares