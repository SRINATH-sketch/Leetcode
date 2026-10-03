class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        arr=[]
        for i in range(left,right+1):
            c=0
            for j in str(i):
                j=int(j)
                if(j==0):
                    break
                if(i%j==0):
                    c+=1
            if(c==len(str(i))):
                arr.append(i)
        return arr