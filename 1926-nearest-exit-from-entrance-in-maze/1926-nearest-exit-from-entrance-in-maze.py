from collections import deque
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        queue=deque([])
        visited=set()

        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        n,m=len(maze),len(maze[0])

        queue.append((entrance[0],entrance[1],0))
        visited.add((entrance[0],entrance[1]))

        while queue:
            row,col,distance=queue.popleft()

            if((row,col)!=(entrance[0],entrance[1])):
                if(row==0 or col==0 or row==n-1 or col==m-1):    
                        return distance
            
            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<n and 0<=nc<m):
                    if(maze[nr][nc]=='.' and (nr,nc) not in visited):
                            visited.add((nr,nc))
                            queue.append((nr,nc,distance+1))    
        return -1