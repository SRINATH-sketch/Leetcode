class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
        c=0
        i=0
        while(i<len(num)):
            if(num[i]=='0'):
                c+=1
            else:
                c=0
            i+=1
        if(c!=0):
            return num[:-c]
        return num