class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(n):
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        n = len(isConnected)
        visited = set()
        components = 0

        for start in range(n):
            if start not in visited:
                components += 1
                dfs(start)

        return components
