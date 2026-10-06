class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        r=len(heights)
        c=len(heights[0])
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        visited_p=set()
        def dfs_p(row,col):
            visited_p.add((row,col))

            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<r and 0<=nc<c):
                    if(heights[row][col]<=heights[nr][nc] and (nr,nc) not in visited_p):
                        dfs_p(nr,nc)

        for i in range(c):
            dfs_p(0,i)
        for j in range(r):
            dfs_p(j,0)

        visited_a=set()
        def dfs_a(row,col):
            visited_a.add((row,col))

            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<r and 0<=nc<c):
                    if(heights[row][col]<=heights[nr][nc] and (nr,nc) not in visited_a):
                        dfs_a(nr,nc)
        
        for i in range(r):
            dfs_a(i,c-1)
        for j in range(c):
            dfs_a(r-1,j)
        
        arr=[]
        for i in visited_p & visited_a:
            arr.append(i)
        return arr