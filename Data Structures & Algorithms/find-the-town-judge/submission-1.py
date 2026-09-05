class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        incoming: List[int] = [0] * (n + 1)
        outgoing: List[int] = [0] * (n + 1)
        for a, b in trust:
            outgoing[a] += 1
            incoming[b] += 1
        for person in range(1, n + 1):
            if incoming[person] == n - 1 and outgoing[person] == 0:
                return person
        return -1