class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k: int = 1
        while True:
            totalHours: int = 0
            for pile in piles:
                totalHours += math.ceil(pile / k)
                if totalHours > h:
                    k += 1
                    break
            if totalHours <= h:
                return k