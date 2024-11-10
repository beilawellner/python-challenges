class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            stack = [start]
            while stack:
                start = stack.pop()
                visited.add(start)
                for end in range(n):
                    if isConnected[start][end] and end not in visited:
                        stack.append(end)

        n = len(isConnected)
        visited = set()
        components = 0

        for start in range(n):
            if start not in visited:
                components += 1
                dfs(start)

        return components
