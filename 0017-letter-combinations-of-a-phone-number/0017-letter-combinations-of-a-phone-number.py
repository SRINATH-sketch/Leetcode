from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters=[
            "","","abc",
            "def","ghi","jkl",
            "mno","pqrs","tuv",
            "wxyz"
        ]

        result=[""]

        for i in digits:
            temp=[]
            for j in result:
                for ch in letters[int(i)]:
                    temp.append(j+ch)

            result=temp

        return result