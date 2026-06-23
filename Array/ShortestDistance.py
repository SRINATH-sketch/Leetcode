class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        check=[]
        s=s.strip()
        for i in range(len(s)):
            if(s[i]==c):
                check.append(i)
        arr1=[]
        for i in range(len(s)):
            m=float('inf')
            for j in check:
                if(i<j):
                    if((j-i)<m):
                        m=(j-i)
                elif(i>j):
                    if((i-j)<m):
                        m=(i-j)
                elif(i==j):
                    m=0
            arr1.append(m)
        return arr1