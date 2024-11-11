class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        def dfs(city):
            nonlocal changes, visited
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    changes += 1
                visited.add(neighbor)
                dfs(neighbor)

        edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        visited = {0}
        changes = 0

        dfs(0)
        return changes
