class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr=""
        s=str(x)
        for i in range(len(s)-1,-1,-1):
            arr+=s[i]
        if(arr==s):
            return True
        else:
            return False