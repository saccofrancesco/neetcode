# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack: List[Tuple[TreeNode, float, float]] = [(root, float("-inf"), float("inf"))]
        while stack:
            node, lower, upper = stack.pop()
            if node is None:
                continue
            if not lower < node.val < upper:
                return False
            stack.append((node.left, lower, node.val))
            stack.append((node.right, node.val, upper))
        return True