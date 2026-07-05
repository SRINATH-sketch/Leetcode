class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def path(i,j,solution,remaining):
            nonlocal c
            if(i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or solution[i][j]==-1 or grid[i][j]==-1):
                return

            solution[i][j]=-1
            remaining-=1
        
            if(grid[i][j]==2):
                if remaining==0:
                    c+=1
                solution[i][j]=0
                return

            path(i+1,j,solution,remaining)
            path(i,j+1,solution,remaining)
            path(i-1,j,solution,remaining)
            path(i,j-1,solution,remaining)

            solution[i][j]=0
            return 

        i=0
        j=0
        remaining=0
        for r in range(len(grid)):
            for c1 in range(len(grid[0])):
                if grid[r][c1]==1:
                    i,j=r,c1
                    break

        for r in range(len(grid)):
            for c1 in range(len(grid[0])):
                if grid[r][c1]!=-1:
                    remaining+=1
                    

        c=0
        solution=[[0]*len(grid[0]) for i in range(len(grid))]
    
        path(i,j,solution,remaining)    
        return c