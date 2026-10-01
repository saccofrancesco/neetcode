class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time: int = 0
        target: int = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], target)
            else:
                time += min(tickets[i], target - 1)
        return time