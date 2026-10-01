class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time: int = 0
        total_waiting: int = 0
        for arrival, time in customers:
            current_time: int = max(current_time, arrival)
            current_time += time
            total_waiting += current_time - arrival
        return total_waiting / len(customers)