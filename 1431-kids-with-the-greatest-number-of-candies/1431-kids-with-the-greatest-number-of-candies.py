class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        arr=[]
        m=max(candies)
        for i in candies:
            if(i+extraCandies>=m):
                arr.append(True)
            else:
                arr.append(False)
        return arr