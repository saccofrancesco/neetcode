class Solution:
    def carPooling(self, trips, capacity):
        passengers: List[int] = [0] * 1001
        for num, start, end in trips:
            passengers[start] += num
            passengers[end] -= num
        current: int = 0
        for change in passengers:
            current += change
            if current > capacity:
                return False
        return True