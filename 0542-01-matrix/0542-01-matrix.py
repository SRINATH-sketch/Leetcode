from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        queue=deque([])
        visited=set()
        n=len(mat)
        m=len(mat[0])
        for i in range(n):
            for j in range(m):
                if(mat[i][j]==0):
                    queue.append((i,j,0))
                    visited.add((i,j))

        while(queue):
            row,col,distance=queue.popleft()
            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<n and 0<=nc<m):
                    if((nr,nc) not in visited):
                        visited.add((nr,nc))
                        mat[nr][nc]=distance+1
                        queue.append((nr,nc,distance+1))
        return mat
