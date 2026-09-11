from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count=set()
        for i in permutations(digits,3):
            if(i[0]!=0 and i[2]%2==0):
                count.add(i)
        return len(count)