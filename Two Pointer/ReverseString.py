class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l1=[]
        l=len(s)
        for i in range(l-1,-1,-1):
            l1.append(s[i])
        for i in range(l):
            s[i]=l1[i]
        