# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        right_view: List[int] = []
        queue = deque([root])
        while queue:
            level_size: int = len(queue)
            for index in range(level_size):
                node: TreeNode = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                if index == level_size - 1:
                    right_view.append(node.val)
        return right_view