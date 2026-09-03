class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0)
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            # Se rubo questo nodo,
            # non posso rubare direttamente i figli
            rob = (
                node.val
                + left_skip
                + right_skip
            )
            # Se non rubo questo nodo,
            # per ogni figlio scelgo l'opzione migliore
            skip = (
                max(left_rob, left_skip)
                + max(right_rob, right_skip)
            )
            return (rob, skip)
        rob_root, skip_root = dfs(root)
        return max(rob_root, skip_root)