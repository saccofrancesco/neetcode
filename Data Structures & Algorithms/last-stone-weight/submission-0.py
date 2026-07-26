import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights: List[int] = stones.copy()
        while len(weights) > 1:
            heaviest, secondHeaviest = heapq.nlargest(2, weights)
            print(heaviest, secondHeaviest)
            if heaviest == secondHeaviest:
                weights.remove(heaviest)
                weights.remove(secondHeaviest)
            elif secondHeaviest < heaviest:
                weights.remove(heaviest)
                weights.remove(secondHeaviest)
                weights.append(heaviest - secondHeaviest)
        return weights[0] if weights else 0
