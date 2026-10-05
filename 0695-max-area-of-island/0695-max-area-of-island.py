class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visited=set()
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(row,col):
            visited.add((row,col))
            island_space=1
            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<n and 0<=nc<m):
                    if(grid[nr][nc]==1 and (nr,nc) not in visited):
                        island_space+=dfs(nr,nc)
            return island_space

        n=len(grid)
        m=len(grid[0])
        largest=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1 and (i,j) not in visited):
                    island_space=dfs(i,j)
                    if(island_space>largest):
                        largest=island_space
        return largest