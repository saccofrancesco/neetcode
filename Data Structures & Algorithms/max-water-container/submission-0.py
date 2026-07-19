class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pairsValues: dict[str, int] = dict()
        for i, b1 in enumerate(heights):
            for j, b2 in enumerate(heights):
                current: int = 0
                distance: int = j - i
                if i == j:
                    continue
                if b1 <= b2:
                    current = abs(b1 * distance)
                else:
                    current = abs(b2 * distance)
                if (f"{i}x{j}" or f"{j}x{i}") in pairsValues:
                    continue
                else:
                    pairsValues[f"{i}x{j}"] = current
        return max(list(pairsValues.values()))