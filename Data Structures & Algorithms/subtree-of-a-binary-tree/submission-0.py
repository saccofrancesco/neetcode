# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(
            node1: Optional[TreeNode],
            node2: Optional[TreeNode]
        ) -> bool:
            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False
            return (
                node1.val == node2.val
                and is_same_tree(node1.left, node2.left)
                and is_same_tree(node1.right, node2.right)
            )
        if root is None:
            return False
        if is_same_tree(root, subRoot):
            return True
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )