class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        perimeter=0

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    perimeter+=4
                
                    if i>0 and grid[i-1][j]==1:
                        perimeter-=1
                    if i<r-1 and grid[i+1][j]==1:
                        perimeter-=1
                    if j>0 and grid[i][j-1]==1:
                        perimeter-=1
                    if j<c-1 and grid[i][j+1]==1:
                        perimeter-=1
                
        return perimeter