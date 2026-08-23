from collections import Counter
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count: Counter = Counter(hand)
        for card in sorted(count):
            occurrences: int = count[card]
            if occurrences > 0:
                for nextCard in range(card, card + groupSize):
                    if count[nextCard] < occurrences:
                        return False
                    count[nextCard] -= occurrences
        return True