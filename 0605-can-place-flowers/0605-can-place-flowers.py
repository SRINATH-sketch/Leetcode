class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n==0:
            return True
        m=len(flowerbed)
        for i in range(m):
            if flowerbed[i]==0:
                l=(i==0 or flowerbed[i-1]==0)
                r=(i==m-1 or flowerbed[i+1]==0)
                if l and r:
                    flowerbed[i]=1
                    n-=1
                
            if(n==0):
                return True
        return False