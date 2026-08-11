from typing import List


class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        # At most k stops means at most k + 1 flights.
        for _ in range(k + 1):
            temp = prices.copy()

            for u, v, price in flights:
                if prices[u] == float("inf"):
                    continue

                temp[v] = min(
                    temp[v],
                    prices[u] + price
                )

            prices = temp

        return -1 if prices[dst] == float("inf") else prices[dst]