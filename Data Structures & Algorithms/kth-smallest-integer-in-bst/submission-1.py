# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack: List[TreeNode] = list()
        node: TreeNode = root
        while True:
            while node is not None:
                stack.append(node)
                node: TreeNode = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node: TreeNode = node.right