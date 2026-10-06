from collections import deque
class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        queue=deque([])
        visited=set()
        r=len(grid)
        c=len(grid[0])
        found=False
        for i in range(r):
            for j in range(c):
                if(grid[i][j]==1):
                    queue.append((i,j))
                    visited.add((i,j))
                    found=True
                    break
            if(found):
                break

        queue1=deque([])

        while(queue):
            row,col=queue.popleft()
            queue1.append((row,col,0))

            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<r and 0<=nc<c):
                    if(grid[nr][nc]==1 and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        
        while(queue1):
            row,col,distance=queue1.popleft()
            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<r and 0<=nc<c):
                    if(grid[nr][nc]==0 and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        queue1.append((nr,nc,distance+1))
                    elif(grid[nr][nc]==1 and (nr,nc) not in visited):
                        return distance
        return -1