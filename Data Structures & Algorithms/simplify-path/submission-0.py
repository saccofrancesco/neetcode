class Solution:
    def simplifyPath(self, path: str) -> str:
        stack: List[int] = list()
        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)