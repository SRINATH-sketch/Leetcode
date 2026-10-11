from collections import deque
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        queue=deque([])
        n,m=len(grid),len(grid[0])
        queue.append((0,0))
        moves=[(0,1,1),(0,-1,2),(1,0,3),(-1,0,4)]
        distance=[[float('inf')]*m for i in range(n)]
        distance[0][0]=0
        
        while queue:
            row,col=queue.popleft()
            for dr,dc,direction in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<n and 0<=nc<m):
                    cost=0
                    if(grid[row][col]!=direction):
                        cost=1
                    new_cost=distance[row][col]+cost
                    if(new_cost<distance[nr][nc]):
                        distance[nr][nc]=new_cost

                        if(cost==0):
                            queue.appendleft((nr,nc))
                        else:
                            queue.append((nr,nc))
        
        return distance[n-1][m-1]