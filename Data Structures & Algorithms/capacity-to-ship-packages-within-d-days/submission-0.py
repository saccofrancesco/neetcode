class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left: int = max(weights)
        right: int = sum(weights)

        while left < right:
            mid: int = (left + right) // 2
            needed_days: int = 1
            current_weight: int = 0
            for weight in weights:
                if current_weight + weight > mid:
                    needed_days += 1
                    current_weight = 0
                current_weight += weight
            if needed_days <= days:
                right = mid
            else:
                left = mid + 1
        return left