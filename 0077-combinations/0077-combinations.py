from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers=[]
        for i in range(1,n+1):
            numbers.append(i)

        arr=[]
        for i in combinations(numbers,k):
            arr.append(i)
        
        return arr