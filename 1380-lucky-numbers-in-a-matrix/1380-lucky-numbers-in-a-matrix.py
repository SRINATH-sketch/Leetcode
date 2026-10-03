class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        m=len(matrix[0])
        lucky=[]
        for i in range(n):
            mini=min(matrix[i])
            for j in range(m):
                if(matrix[i][j]==mini):
                    arr=[]
                    for k in range(n):
                        arr.append(matrix[k][j])
                    if(max(arr)==mini):
                        lucky.append(mini)
        return lucky