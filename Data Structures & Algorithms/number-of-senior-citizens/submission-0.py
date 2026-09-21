class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count: int = 0
        for passenger in details:
            age: int = int(passenger[11:13])
            if age > 60:
                count += 1
        return count