class Solution:
    def checkRecord(self, s: str) -> bool:
        a,l=0,0
        for i in s:
            if(i=='P'):
                l=0
            if(i=='A'):
                a+=1
                l=0
            elif(i=='L'):
                l+=1
            if(a>=2 or l>=3):
                return False
        return True