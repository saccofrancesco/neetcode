# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good: int = 0
        def dfs(node: TreeNode, path_max: int) -> None:
            nonlocal good
            if node.val >= path_max:
                good += 1
                path_max = node.val
            if node.left:
                dfs(node.left, path_max)
            if node.right:
                dfs(node.right, path_max)
        dfs(root, root.val)
        return good