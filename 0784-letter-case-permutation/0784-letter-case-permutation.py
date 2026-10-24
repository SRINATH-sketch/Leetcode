from itertools import permutations
class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result=[""]
        for i in s:
            temp=[]
            for j in result:
                if(i.isalpha()):
                    temp.append(j+i.lower())
                    temp.append(j+i.upper())
                else:
                    temp.append(j+i)
            result=temp
        return result