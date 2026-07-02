class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        arr=set()
        result=set()
        for i in range(len(s)-10+1):
            check=s[i:i+10]
            if(check in arr):
                result.add(check)
            else:
                arr.add(check)

        return list(result)