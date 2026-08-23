class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas: int = 0
        currentGas: int = 0
        start: int = 0
        for i in range(len(gas)):
            difference: int = gas[i] - cost[i]
            totalGas += difference
            currentGas += difference
            if currentGas < 0:
                start = i + 1
                currentGas = 0
        return start if totalGas >= 0 else -1