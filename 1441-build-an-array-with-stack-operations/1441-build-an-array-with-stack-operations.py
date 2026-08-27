class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        rans=[]
        for i in range(1,n+1):
            if(rans==target):
                break
            elif(i in target):
                ans.append("Push")
                rans.append(i)
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans