from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        queue=deque([])
        visited=set()
        r=len(board)
        c=len(board[0])
        for i in range(r):
            for j in range(c):
                if(board[i][j]=='O' and (i==0 or j==0 or i==r-1 or j==c-1)):
                    queue.append((i,j))
                    visited.add((i,j))
        
        while(queue):
            row,col=queue.popleft()
            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<r and 0<=nc<c):
                    if(board[nr][nc]=='O' and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        
        for i in range(r):
            for j in range(c):
                if(board[i][j]=='O' and (i,j) not in visited):
                    board[i][j]='X'
        