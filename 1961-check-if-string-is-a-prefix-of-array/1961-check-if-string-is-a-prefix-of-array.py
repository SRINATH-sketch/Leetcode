class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        string=""
        m=len(words)
        for i in words:
            string+=i
    
            if(string==s):
                return True

            if(len(string)>len(s)):
                return False

        return False