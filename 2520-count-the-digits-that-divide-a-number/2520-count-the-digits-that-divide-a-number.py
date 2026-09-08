class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        temp=num
        while(temp>0):
            q=temp%10
            if(num%q==0):
                c+=1
            temp=temp//10
        return c