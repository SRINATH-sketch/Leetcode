class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict={}
        result=[]
        for i in range(len(s)-10+1):
            check=s[i:i+10]
            if(check in dict):
                dict[check]+=1
            else:
                dict[check]=1
            if(dict[check]==2):
                result.append(check)

        return result