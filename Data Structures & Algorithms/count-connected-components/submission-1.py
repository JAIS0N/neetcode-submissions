class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
    
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        for u, v in edges:
            union(u, v)
        
        # Count unique roots
        return len(set(find(i) for i in range(n)))