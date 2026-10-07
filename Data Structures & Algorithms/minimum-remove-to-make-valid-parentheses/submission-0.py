class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        # Any "(" left in the stack has no matching ")"
        remove.update(stack)
        result = []
        for i, char in enumerate(s):
            if i not in remove:
                result.append(char)
        return "".join(result)