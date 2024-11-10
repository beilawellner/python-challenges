'''
[[1,3],[3,0,1],[2],[0]]
stack = [1]
visited = (0, 3)
i = 1
'''
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        i = 0
        visited = {0}
        stack = rooms[0]
        while stack:
            i = stack.pop()
            for key in rooms[i]:
                if key not in visited:
                    stack.append(key)
            visited.add(i)
        return len(visited) == len(rooms)
