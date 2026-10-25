from collections import deque
class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n,m=len(grid),len(grid[0])
        queue=deque([])
        visited=set()
        queue.append((0,0))
        visited.add((0,0))

        moves=[(-1,0),(1,0),(0,-1),(0,1)]

        def bfs(i,j):
            closed=True
            queue=deque([(i,j)])
            visited.add((i,j))
            while queue:
                row,col=queue.popleft()

                if(row==0 or col==0 or row==n-1 or col==m-1):
                    closed=False

                for dr,dc in moves:
                    nr=dr+row
                    nc=dc+col
                    if(0<=nr<n and 0<=nc<m):
                        if(grid[nr][nc]==0 and (nr,nc) not in visited):
                            queue.append((nr,nc))
                            visited.add((nr,nc))  
            return closed

        count=0

        for i in range(n):
            for j in range(m):
                if(grid[i][j]==0 and (i,j) not in visited):
                    if(bfs(i,j)):
                        count+=1
        return count