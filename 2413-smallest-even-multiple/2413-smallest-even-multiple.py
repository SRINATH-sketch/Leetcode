class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        m=n
        while(m%2!=0 or m%n!=0):
            m+=1
        return m