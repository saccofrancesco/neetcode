# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index: Dict[int, int] = {
            value: index
            for index, value in enumerate(inorder)
        }
        preorder_index: int = 0
        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal preorder_index
            if left > right:
                return None
            root_value: int = preorder[preorder_index]
            preorder_index += 1
            root: TreeNode = TreeNode(root_value)
            middle: int = inorder_index[root_value]
            root.left: Optional[TreeNode] = build(left, middle - 1)
            root.right: Optional[TreeNode] = build(middle + 1, right)
            return root
        return build(0, len(inorder) - 1)