from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        arr=[1,2,3,4,5,6,7,8,9]
        result=[]
        for i in combinations(arr,k):
            if(sum(i)==n):
                result.append(i)
        return result