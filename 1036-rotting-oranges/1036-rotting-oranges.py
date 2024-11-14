class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Step 1: Initialize the queue with all rotten oranges and count fresh oranges.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        # If there are no fresh oranges, return 0.
        if fresh_count == 0:
            return 0

        # Step 2: Perform BFS from initially rotten oranges.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        while queue and fresh_count > 0:
            minutes += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    # If the neighboring cell has a fresh orange, rot it.
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        queue.append((nx, ny))

        # If there are still fresh oranges, return -1; otherwise, return the minutes elapsed.
        return minutes if fresh_count == 0 else -1
