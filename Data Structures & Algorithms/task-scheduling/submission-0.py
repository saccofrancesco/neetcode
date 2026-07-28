class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        max_frequency: int = max(frequencies.values())
        most_frequent_count: int = sum(
            frequency == max_frequency
            for frequency in frequencies.values()
        )
        required_cycles = (
            (max_frequency - 1) * (n + 1)
            + most_frequent_count
        )
        return max(len(tasks), required_cycles)