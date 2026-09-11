class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        c1=set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if(i!=j and j!=k and k!=i):
                        if(digits[i]!=0 and digits[k]%2==0):
                            c1.add((digits[i],digits[j],digits[k]))
        return len(c1)