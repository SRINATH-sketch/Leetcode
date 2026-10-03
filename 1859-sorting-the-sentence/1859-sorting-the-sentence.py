class Solution:
    def sortSentence(self, s: str) -> str:
        arr=[None]*len(s.split())
        for i in s.split():
            m=len(i)
            num=int(i[m-1])
            arr[num-1]=i[:-1]
        return " ".join(arr)