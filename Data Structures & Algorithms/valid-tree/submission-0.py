class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visiting = set()
        visited  = set()

        def dfs(node, parent):
            if node in visiting:   # cycle detected
                return False

            visiting.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:  # skip the edge we came from
                    continue
                if not dfs(neighbor, node):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n   # all nodes reachable