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
            # (px, py) must be diagonally opposite to (x, y)
            if px == x or py == y:
                continue

            # A square must have equal width and height
            if abs(px - x) != abs(py - y):
                continue

            # Other two corners:
            # (px, y) and (x, py)
            squares += (
                freq
                * self.points[(px, y)]
                * self.points[(x, py)]
            )

        return squares