from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        queue=deque([])
        visited=set()

        n=len(grid)
        m=len(grid[0])
        fresh=0
        time=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==2):
                    queue.append((i,j,0))
                    visited.add((i,j))
                elif(grid[i][j]==1):
                    fresh+=1
        
        while(queue):
            row,col,time=queue.popleft()
            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if((0<=nr<n and 0<=nc<m) and (nr,nc) not in visited):
                    if(grid[nr][nc]==1):
                        visited.add((nr,nc))
                        queue.append((nr,nc,time+1))
                        fresh-=1
        if(fresh==0):
            return time
        return -1