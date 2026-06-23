# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=[]
        if(len(s)!=len(t)):
            return False
        for i in s:
            if(i in t):
                l.append(i)
                t=t.replace(i,"",1)
            else:
                return False
    
        if(len(l)==len(s)):
            return True