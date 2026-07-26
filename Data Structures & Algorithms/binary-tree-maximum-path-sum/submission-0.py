# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum: float = float("-inf")
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal maximum
            if node is None:
                return 0
            left_gain: int = max(0, dfs(node.left))
            right_gain: int = max(0, dfs(node.right))
            path_sum: int = left_gain + node.val + right_gain
            maximum = max(maximum, path_sum)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return maximum