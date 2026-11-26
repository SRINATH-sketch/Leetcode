class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        n,m=len(board),len(board[0])
        moves=[(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(row,col,index):
            if(board[row][col]!=word[index]):
                return False

            if(index==len(word)-1):
                return True

            temp=board[row][col]
            board[row][col]='#'

        
            for dr,dc in moves:
                nr=dr+row
                nc=dc+col
                if(0<=nr<n and 0<=nc<m):
                    if dfs(nr,nc,index+1):
                        board[row][col]=temp
                        return True

            board[row][col]=temp
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row,col,0):
                    return True
        return False