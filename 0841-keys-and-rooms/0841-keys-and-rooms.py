from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited=set()
        def dfs(mr):
            visited.add(mr)

            for i in rooms[mr]:
                if(i not in visited):
                    dfs(i)

        dfs(0)
        if(len(visited)==len(rooms)):
            return True
        return False