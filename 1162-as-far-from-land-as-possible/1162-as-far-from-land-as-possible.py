from collections import deque
class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        queue=deque([])
        visited=set()
        r=len(grid)
        c=len(grid[0])
        water=0
        for i in range(r):
            for j in range(c):
                if(grid[i][j]==1):
                    queue.append((i,j,0))
                    visited.add((i,j))
                elif(grid[i][j]==0):
                    water+=1

        if(len(queue)==0 or water==0):
            return -1

        while(queue):
            row,col,distance=queue.popleft()
            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<r and 0<=nc<c):
                    if(grid[nr][nc]==0 and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        queue.append((nr,nc,distance+1))
                        grid[nr][nc]+=distance+1
        
        m=0
        for i in range(r):
            for j in range(c):
                if(grid[i][j]>m):
                    m=grid[i][j]
        return m