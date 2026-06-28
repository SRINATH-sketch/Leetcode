from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        k=len(s1)
        c1=Counter(s2[:k])
        if(c1==Counter(s1)):
            return True
        for i in range(k,len(s2)):
            c1[s2[i]]+=1
            c1[s2[i-k]]-=1
            if(c1==Counter(s1)):
                return True
        return False