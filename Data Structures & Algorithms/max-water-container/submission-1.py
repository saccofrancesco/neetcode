class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for left in range(len(heights)):
            for right in range(left + 1, len(heights)):
                width = right - left
                height = min(heights[left], heights[right])
                max_area = max(max_area, width * height)

        return max_area