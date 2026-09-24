class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best: str = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                candidate: str = num[i:i + 3]
                best = max(best, candidate)
        return best