class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # b1=[]
        # b2=[]
        # max1=0
        # for i in range(len(fruits)):
        #     if(len(b1)==0 or fruits[i] in b1):
        #         b1.append(fruits[i])
        #     elif(len(b2)==0 or fruits[i] in b2):
        #         b2.append(fruits[i])
        #     else:
        #         if(not fruits[i+1] in b1):
        #             b1.clear()
        #             b1.append(fruits[i])
        #         else:
        #             b2.clear()
        #             b2.append(fruits[i])
        #     m=len(b1)+len(b2)
        #     max1=max(m,max1)
        # return max1
        i=0
        d={}
        m=0
        for j in range(len(fruits)):
            d[fruits[j]]=d.get(fruits[j],0)+1
            while(len(d)>2):
                d[fruits[i]]-=1
                if(d[fruits[i]]==0):
                    del d[fruits[i]]
                i+=1
            m=max(m,j-i+1)
        return m