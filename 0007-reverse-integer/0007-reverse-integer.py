class Solution:
    def reverse(self, x: int) -> int:
        ans=0
        m=str(x)
        if(x<0):
            ans=-int(m[1:][::-1])
        else:
            ans=int(m[::-1])
        if(ans>2147483648 or ans<-2147483647):
            return 0
        
        return ans