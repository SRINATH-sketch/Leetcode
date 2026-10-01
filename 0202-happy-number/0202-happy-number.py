class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while(n!=1):
            s=0
            if n in seen:
                return False
            seen.add(n)

            while(n>0):
                num=n%10
                square=num*num
                s+=square
                n=n//10
            n=s
        return True