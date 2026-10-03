class Solution:
    def reverseWords(self, s: str) -> str:
        sums=""
        n=len(s)
        for i in s.split():
            sums+=i[::-1]
            sums+=" "
        
        return sums[:-1]