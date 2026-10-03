class Solution:
    def countAsterisks(self, s: str) -> int:
        outside=True
        asterisks=0
        for i in s:
            if(i=='|'):
                if(outside==False):
                    outside=True
                elif(outside==True):
                    outside=False
            if(outside and i=='*'):
                asterisks+=1
        return asterisks