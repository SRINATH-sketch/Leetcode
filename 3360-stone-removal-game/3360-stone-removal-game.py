class Solution:
    def canAliceWin(self, n: int) -> bool:
        a=10
        while(n>=a):
            n-=a
            a-=1
        if(a%2==1):
            return True
        else:
            return False