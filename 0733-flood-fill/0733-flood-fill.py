moves=[(-1,0),(1,0),(0,-1),(0,1)]
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int,visited=None) -> list[list[int]]:
        if visited is None:
            visited=set()
        original=image[sr][sc]
        n=len(image)
        m=len(image[0])
        if(original==color):
            return image
        visited.add((sr,sc))
        image[sr][sc]=color
        for dr,dc in moves:
            nr=dr+sr
            nc=dc+sc
            if(0<=nr<n and 0<=nc<m):
                if(image[nr][nc]==original and (nr,nc) not in visited):
                    self.floodFill(image,nr,nc,color,visited)
        return image