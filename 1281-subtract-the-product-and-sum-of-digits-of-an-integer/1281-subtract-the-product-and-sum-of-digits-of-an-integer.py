class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m=1
        s=0
        m1=n
        while(m1):
            r=m1%10
            m*=r
            s+=r
            m1=m1//10
        return m-s