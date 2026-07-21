class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[str] = list()
        for tkn in tokens:
            if tkn in "+-*/":
                n1: int = stack.pop()
                n2: int = stack.pop()
                result: int = math.floor(eval(f"{n2} {tkn} {n1}"))
                stack.append(result)
            else:
                stack.append(tkn)
        return stack[0]