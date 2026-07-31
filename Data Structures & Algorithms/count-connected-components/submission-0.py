class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph: List[List[int]] = [[] for _ in range(n)]
        for node_a, node_b in edges:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)
        visited: set[int] = set()
        components: int = 0
        for node in range(n):
            if node in visited:
                continue
            components += 1
            queue = deque([node])
            visited.add(node)
            while queue:
                current: int = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return components
