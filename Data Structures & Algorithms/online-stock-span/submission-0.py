class StockSpanner:

    def __init__(self):
        self.stack: List[int] = list()

    def next(self, price: int) -> int:
        span: int = 1
        while self.stack and self.stack[-1][0] <= price:
            previous_price, previous_span = self.stack.pop()
            span += previous_span
        self.stack.append((price, span))
        return span