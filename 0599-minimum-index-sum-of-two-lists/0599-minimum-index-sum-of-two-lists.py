class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        res=[]
        d={}
        for i in range(len(list1)):
            s=0
            for j in range(len(list2)):
                if(list1[i]==list2[j]):
                    s=i+j
                    d[list1[i]]=s
        mini=min(d.values())
        for x,y in d.items():
            if(y==mini):
                res.append(x)
        return res