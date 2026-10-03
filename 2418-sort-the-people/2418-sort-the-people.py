class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        arr=list(zip(heights,names))
        arr.sort(reverse=True)
        result=[]
        for x,y in arr:
            result.append(y)
        return result