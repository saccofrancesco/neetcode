class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area: int = 0
        stack: list[tuple[int, int]] = list()
        for i, height in enumerate(heights):
            start: int = i
            while stack and stack[-1][1] > height:
                index, previous_height = stack.pop()
                width: int = i - index
                max_area: int = max(max_area, previous_height * width)
                start: int = index
            stack.append((start, height))
        for index, height in stack:
            width: int = len(heights) - index
            max_area: int = max(max_area, height * width)
        return max_area