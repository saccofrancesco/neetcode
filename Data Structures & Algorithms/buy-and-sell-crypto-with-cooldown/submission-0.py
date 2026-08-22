class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        hold: int = -prices[0]
        sold: int = 0
        rest: int = 0
        for price in prices[1:]:
            prev_hold: int = hold
            prev_sold: int = sold
            prev_rest: int = rest
            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)
        return max(sold, rest)