class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime=0
        for i in range(left,right+1):
            b=bin(i)[2:]
            c=0
            for j in str(b):
                if(j=='1'):
                    c+=1

            count=0

            for k in range(1,c+1):
                if(c%k==0):
                    count+=1
            if(count==2):
                prime+=1
        return prime