from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n: int = len(senate)
        radiant: deque = deque()
        dire: deque = deque()
        for i, senator in enumerate(senate):
            if senator == "R":
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r: str = radiant.popleft()
            d: str = dire.popleft()
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"