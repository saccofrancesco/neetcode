# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], path_max: int) -> int:
            if node is None:
                return 0
            is_good: int = 1 if node.val >= path_max else 0
            new_max: int = max(path_max, node.val)
            return (
                is_good
                + dfs(node.left, new_max)
                + dfs(node.right, new_max)
            )
        return dfs(root, root.val)