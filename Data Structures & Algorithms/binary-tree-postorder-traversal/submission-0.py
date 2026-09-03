class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result: List[int] = list()
        stack: List[Tuple[TreeNode, bool]] = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        return result