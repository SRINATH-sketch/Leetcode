from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        moves=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        queue=deque([])
        visited=set()
        
        n=len(grid)
        m=len(grid[0])
    
        if(grid[0][0]==1 or grid[n-1][m-1]):
            return -1

        queue.append((0,0,1))
        visited.add((0,0))

        while(queue):
            row,col,distance=queue.popleft()
            if(row==n-1 and col==m-1):
                return distance
            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<n and 0<=nc<m):
                    if(grid[nr][nc]==0 and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        queue.append((nr,nc,distance+1))
        return -1