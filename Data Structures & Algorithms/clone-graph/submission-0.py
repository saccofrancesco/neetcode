"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clones = {}
        def dfs(original: Node) -> Node:
            if original in clones:
                return clones[original]
            clone = Node(original.val)
            clones[original] = clone
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)
