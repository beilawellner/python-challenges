class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                visited.add(current)
                for neighbor in range(n):
                    if isConnected[current][neighbor] == 1 and neighbor not in visited:
                        stack.append(neighbor)

        n = len(isConnected)
        visited = set()
        components = 0

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components
