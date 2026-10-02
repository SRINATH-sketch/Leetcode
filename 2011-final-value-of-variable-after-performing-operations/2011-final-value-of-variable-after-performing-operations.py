class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x=0
        for i in operations:
            if "+" in i:
                x+=1
            else:
                x-=1
        return x