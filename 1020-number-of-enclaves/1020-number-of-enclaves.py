from collections import deque
class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        r,c=len(grid),len(grid[0])
        queue=deque([])
        visited=set()
        for i in range(r):
            for j in range(c):
                if(grid[i][j]==1 and (i==0 or i==r-1 or j==0 or j==c-1)):
                    queue.append((i,j))
                    visited.add((i,j))
    
        while(queue):
            row,col=queue.popleft()
            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<r and 0<=nc<c):
                    if(grid[nr][nc]==1 and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        
        count=0
        for i in range(r):
            for j in range(c):
                if(grid[i][j]==1 and (i,j) not in visited):
                    count+=1
        return count
        